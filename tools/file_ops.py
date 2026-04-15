import os

def create_file(filename):
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)

    with open(path, "w") as f:
        f.write("")

    return f"File created at {path}"