import os
import shutil
from pathlib import Path


def main():
    root = Path()
    output_dir = root / "tmp"

    if output_dir.exists():
        shutil.rmtree(output_dir)

    for path in root.rglob("cookiecutter.json"):
        path = path.parent
        # Ignore bootstrapped templates
        if "{{" not in str(path) and "}}" not in str(path):
            continue

        assert (
            os.system(f"cookiecutter {path} --no-input --output-dir {output_dir}") == 0
        ), f"cookiecutter template {path} failed!"
        shutil.rmtree(output_dir)


if __name__ == "__main__":
    main()
