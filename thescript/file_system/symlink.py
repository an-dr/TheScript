import os
from thescript import path_u


def symlink(source, destination):
    os.symlink(path_u(source), path_u(destination))


if __name__ == '__main__':
    symlink("C:\\Users", "C:\\us2")
