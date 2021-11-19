import json
from pathlib import Path

def main():
    root = Path(__file__).parent
    dirs = []
    for path in root.rglob("cookiecutter.json"):
        dirs.append(str(path.parent).replace(str(root) + "/", ""))

    dirs = sorted(dirs)

    with open(root / "info.json", "w") as f:
        json.dump({"dirs": dirs}, f, indent=2)

if __name__ == '__main__':
    main()