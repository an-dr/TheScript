from thescript import path_u
import os

def touch(path):
    if not os.path.exists(path_u(path)):
        f = open(path_u(path), "w+")
        f.close()


if __name__ == '__main__':
    touch("~/.env")
