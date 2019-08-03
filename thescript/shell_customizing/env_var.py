from thescript import touch, path_u, C


def _parse_dotenv(dotenv_path):
    vars = {}
    with open(path_u(dotenv_path), "r") as f:
        for l in f.readlines():
            parts = l.split("=", maxsplit=2)
            if parts:
                var = parts[0].strip()
                val = parts[1].strip()
                vars.update({var: val})
    return vars


def _write_dotenv(dotenv_path, vars_dict):
    """

    Parameters
    ----------
    dotenv_path : str
    vars_dict : dict

    Returns
    -------

    """
    text = ""
    for k, v in vars_dict.items():
        text += k + "=" + v + "\n"
    with open(path_u(dotenv_path),"w") as f:
        f.write(text)


def env_var(name, value=None):
    if not C.WINDOWS:
        if value is not None:
            pass
        else:
            pass
    else:
        E = "~/.env"
        touch(E)
        vars = _parse_dotenv(E)
        if value is not None:
            vars.update({name: value})
        else:
            try:
                del vars[name]
            except Exception as e:
                print(e)

        _write_dotenv(E, vars)


if __name__ == '__main__':
    env_var("TEST_VAR", "TESTVALNEW")
