def pprint(c):
    print(f"{c.__class__}:")
    if isinstance(c, str):
        print(c)
        return
    c_cap = set(c.__dir__())
    c_dict = {"keys", "values", "items", "__getitem__"}
    c_iterable = {"__iter__"}
    c_str = {"__str__"}
    a_leq = lambda a: (lambda b: a <= b)
    evals = [
        (a_leq(c_dict), lambda x: [f"'{key}' --> '{x[key]}'" for key in sorted(x.keys())]),
        (a_leq(c_iterable), lambda x: [f"[{idx}] --> '{val}'" for idx, val in enumerate(x)]),
        (a_leq(c_str), lambda x: [f"'{str(x)}'"])
    ]
    out = None
    for pred, lame in evals:
        if pred(c_cap):
            out = lame(c)
            break
    for x in out: print(x)


def env_to_be():
    d = {
        "py_maj_min": "3.6",
        "target_env": "mast_env",
        "conda_prefix": "/root/miniconda3"
    }
    d["env_prefix"] = f"{d['conda_prefix']}/envs/{d['target_env']}"
    d["py_lib_prefix"] = f"{d['env_prefix']}/lib/python{d['py_maj_min']}"
    return d


def update_include_path(d):
    import sys
    py_lib_prefix = d["py_lib_prefix"]
    sys_path_pre = [py_lib_prefix, f"{py_lib_prefix}/lib-dynload", f"{py_lib_prefix}/site-packages"]
    for x in sys_path_pre: print(x)
    pth_set_coll = set(sys.path) & set(sys_path_pre)
    for x in pth_set_coll:
        sys_path_pre.remove(x)
    for x in reversed(sys_path_pre):
        sys.path.insert(0, x)
    pprint(sys.path)


def update_path(d):
    import os
    pth0 = os.environ["PATH"].split(":")
    conda_prefix = d["conda_prefix"]
    env_prefix = d["env_prefix"]
    pth_pre = [f"{env_prefix}/bin", f"{conda_prefix}/condabin"]
    # detecting collisions
    pth_set_coll = set(pth0) & set(pth_pre)
    # if any - we do want to prioritize pth_pre, hence removal of collisions from org. path
    for x in pth_set_coll:
        pth0.remove(x)
    pth = ":".join(pth_pre + pth0)
    print(pth)
    os.environ["PATH"] = pth


def set_envs(d):
    import os
    conda_prefix = d["conda_prefix"]
    env_prefix = d["env_prefix"]
    vvv = {
        "CONDA_DEFAULT_ENV": d["target_env"],
        "CONDA_EXE": f"{conda_prefix}/bin/conda",
        "CONDA_PREFIX": env_prefix,
        "CONDA_PREFIX_1": f"{conda_prefix}",
        "CONDA_PYTHON_EXE": f"{conda_prefix}/bin/python",
    }
    for k, v in vvv.items():
        os.environ[k] = v


def go_conda():
    d = env_to_be()
    update_include_path(d)
    update_path(d)
    set_envs(d)
