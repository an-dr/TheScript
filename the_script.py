"""
The Script : https://github.com/an-dr/TheScript
"""


class X:
    """
    The Script's Class: https://github.com/an-dr/TheScript
    """
    from os.path import realpath, basename, dirname, join
    from os.path import join as joinpath
    from os import system as x, environ as env
    from psutil import MACOS, WINDOWS, LINUX
    from subprocess import Popen as shell
    from sys import stdout

    def __init__(self, cmd, script_name):
        self.cmd,  self.__script_dir, self.__script_name = self.__cfg(cmd)
        #
        self.__add_name_window_cmd(script_name)
        self.__add_cd_to_start_dir()
        try: 
            self.__run()
        except KeyboardInterrupt:
            pass
        self.__press_enter()

    def __cfg(self, cmd):
        script_dir, script_name = X.dirname(X.realpath(__file__)),\
            X.basename(__file__)
        if isinstance(cmd, list):
            self.cmd = cmd
        else:
            self.cmd = [cmd]
        return cmd, script_dir, script_name

    def __add_name_window_cmd(self, script_name):
        if X.WINDOWS:
            CH_WIN_NAME = "$host.ui.RawUI.WindowTitle = \"%s\"" % script_name
        elif X.MACOS or X.LINUX:
            CH_WIN_NAME = "echo -ne \"\\033]0;%s\\007\"" % script_name
        self.cmd.insert(0, CH_WIN_NAME)  # add window rename cmd

    def __add_cd_to_start_dir(self):
        self.cmd.insert(0, "cd " + self.__script_dir)  # add window rename cmd

    def __press_enter(self):
        input("%s is finished. Press Enter to close..." % self.__script_name)

    def __run(self):
        if X.WINDOWS:
            SHELL, NEXT_CMD = "powershell", ";"
        elif X.MACOS or X.LINUX:
            SHELL, NEXT_CMDCMD = "sh", ";"
        #
        X.shell([SHELL, NEXT_CMD.join(self.cmd)],
                stdout=X.stdout).communicate()


if __name__ == "__main__":
    X([
        "ls",
        # add commands here
    ],
    __file__)
