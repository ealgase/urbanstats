import ast
import os
import shutil


current = __file__
fixed_py_file = os.path.join(os.path.dirname(current), "fixed.py")


def load_fixed_py():
    with open(fixed_py_file, "r") as f:
        fixed_py = f.read()
    tree = ast.parse(fixed_py)
    tree = tree.body
    assert all(isinstance(x, ast.Assign) for x in tree)
    # go from tree to dict
    fixed = {}
    for x in tree:
        assert len(x.targets) == 1
        key = x.targets[0].id
        value = x.value
        fixed[key] = value.n
    return fixed


def save_fixed_py(fixed):
    with open(fixed_py_file, "w") as f:
        f.write("\n")
        for key, value in fixed.items():
            f.write(f"{key} = {value}\n")


def copy_up_to(site_folder, key, new_up_to):
    source_folder = {
        "juxtastat": "quiz",
        "retrostat": "retrostat",
    }[key]
    dest_folder = {
        "juxtastat": "quiz_old",
        "retrostat": "retrostat_old",
    }[key]
    fixed_py = load_fixed_py()
    for retrostat_week in range(fixed_py[key], new_up_to + 1):
        source = os.path.join(site_folder, source_folder, str(retrostat_week))
        dest = os.path.join(dest_folder, str(retrostat_week))
        print(f"Copying {source} to {dest}")
        shutil.copyfile(source, dest)
    fixed_py[key] = new_up_to
    save_fixed_py(fixed_py)
    os.system(f"git add {dest_folder} {fixed_py_file}")


if __name__ == "__main__":
    import fire

    fire.Fire(copy_up_to)
