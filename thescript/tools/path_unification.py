from os.path import expanduser


def path_u(in_str):
    """

    Parameters
    ----------
    in_str

    Returns
    -------
    output : str
    """
    output = in_str.strip()
    output = output.replace("\\\\", "/")
    output = output.replace("\\", "/")
    output = output.rstrip("/")
    output = output.replace("//", "/")
    output = expanduser(output)
    return output


if __name__ == '__main__':
    test_path1 = "C:\\\\Users\\Cooluser/Documents\\"
    test_path2 = "~\\\\/Documents\\\\document.docx/"
    test_path3 = "/home/user\\\\start.sh"
    print(path_u(test_path1))
    print(path_u(test_path2))
    print(path_u(test_path3))
