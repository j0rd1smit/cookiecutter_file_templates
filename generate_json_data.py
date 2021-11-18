import json
from pathlib import Path

def main():
    root = Path(__file__).parent
    dirs = [path.parent.name for path in root.rglob("cookiecutter.json")]

    with open(root / "info.json", "w") as f:
        json.dump({"dirs": dirs}, f, indent=2)

if __name__ == '__main__':
    main()