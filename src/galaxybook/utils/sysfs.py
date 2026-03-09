def read(path):
    with open(path) as f:
        return f.read().strip()


def write(path, value):
    with open(path, "w") as f:
        f.write(str(value))