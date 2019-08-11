from os import system, environ
import win32con
from win32gui import SendMessage
from winreg import (
    CloseKey, OpenKey, QueryValueEx, SetValueEx,
    HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,
    KEY_ALL_ACCESS, KEY_READ, REG_EXPAND_SZ, REG_SZ
)


def env_keys(user=True):
    if user:
        root = HKEY_CURRENT_USER
        subkey = 'Environment'
    else:
        root = HKEY_LOCAL_MACHINE
        subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    return root, subkey


def get_winenv(name, user=True):
    root, subkey = env_keys(user)
    key = OpenKey(root, subkey, 0, KEY_READ)
    try:
        value, _ = QueryValueEx(key, name)
    except WindowsError:
        return ''
    return value


def set_winenv(name, value):
    key = OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
    CloseKey(key)
    SendMessage(
        win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')


def remove_winenv(paths, value):
    while value in paths:
        paths.remove(value)


def unique(paths):
    unique = []
    for value in paths:
        if value not in unique:
            unique.append(value)
    return unique


def prepend_winenv(name, values):
    for value in values:
        paths = get_winenv(name).split(';')
        remove_winenv(paths, '')
        paths = unique(paths)
        remove_winenv(paths, value)
        paths.insert(0, value)
        set_winenv(name, ';'.join(paths))


def append_winenv(name, values):
    for value in values:
        paths = get_winenv(name).split(';')
        remove_winenv(paths, '')
        paths = unique(paths)
        remove_winenv(paths, value)
        paths.append(value)
        set_winenv(name, ';'.join(paths))


def prepend_winenv_pathext(values):
    prepend_winenv('PathExt_User', values)
    pathext = ';'.join([
        get_winenv('PathExt_User'),
        get_winenv('PathExt', user=False)
    ])
    set_winenv('PathExt', pathext)


def append_winenv_pathext(values):
    append_winenv('PathExt_User', values)
    pathext = ';'.join([
        get_winenv('PathExt_User'),
        get_winenv('PathExt', user=False)
    ])
    set_winenv('PathExt', pathext)


if __name__ == '__main__':
    set_winenv('Home1', '%HomeDrive%%HomePath%')
    set_winenv('Docs1', '%HomeDrive%%HomePath%\docs')
    set_winenv('Prompt1', '$P$_$G$S')

    # prepend_env('Path', [
    #     r'%SystemDrive%\cygwin\bin',  # Add cygwin binaries to path
    #     r'%HomeDrive%%HomePath%\bin',  # shortcuts and 'pass-through' bat files
    #     r'%HomeDrive%%HomePath%\docs\bin\mswin',  # copies of standalone executables
    # ])

    # allow running of these filetypes without having to type the extension
    prepend_winenv_pathext(['.lnk', '.exe.lnk', '.py'])
