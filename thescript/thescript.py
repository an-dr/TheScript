"""
The Script : https://github.com/an-dr/TheScript
"""


class X:
    """
    The Script's Class: https://github.com/an-dr/TheScript

    """
    # path_real() - resolve all path conventions
    from os.path import realpath as path_real
    # path_last() - return the last path name (file.any or dir_name)
    from os.path import basename as path_last
    # path_prefix() - all before the past_last
    from os.path import dirname as path_prefix
    # path_join(a,b,..) - just os.path.join()
    from os.path import join as path_join
    # x() send str to system shell and run
    from os import system as x
    # env["varname"] - dict with envvars
    from os import environ as env
    # cd() - change directory
    from os import chdir as cd
    # dot() - returns current working directory
    from os import getcwd as dot
    # bools for specify OS
    from psutil import MACOS, WINDOWS, LINUX
    # shell process
    from subprocess import Popen as shell
    from sys import stdout

    def __init__(self, cmd, script_name="Sctipt", cwd="."):
        self.cmd,  self.__script_dir, self.__script_name = self.__cfg(cmd)
        self.cwd = X.path_real(cwd)
        #
        self.__add_name_window_cmd(script_name)
        self.__add_cd_to_start_dir()
        try: 
            self.__run()
        except KeyboardInterrupt:
            pass
        self.__press_enter()

    def __cfg(self, cmd):
        script_dir, script_name = X.path_prefix(X.path_real(__file__)),\
            X.path_last(__file__)
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
        X.cd(self.cwd)
        self.cmd.insert(0, "cd " + X.path_real(self.cwd))  # add window rename cmd

    def __press_enter(self):
        input("%s is finished. Press Enter to close..." % self.__script_name)

    def __run(self):
        if X.WINDOWS:
            SHELL, NEXT_CMD = "powershell", ";"
        elif X.MACOS or X.LINUX:
            SHELL, NEXT_CMDCMD = "sh", ";"
        #
        print("INFO: Current Workin DIrectory is " + self.cwd)
        X.shell([SHELL, NEXT_CMD.join(self.cmd)],
                stdout=X.stdout, cwd=self.cwd).communicate()


if __name__ == "__main__":
    X([
        "ls",
        # add commands here
    ],
    __file__)
