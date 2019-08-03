from thescript import path_u


def to_file(in_path, text, append=False):
    if append:
        f = open(path_u(in_path), "a")
    else:
        f = open(path_u(in_path), "w")
    f.write(text)
    f.close()
