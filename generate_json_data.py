import json
import pprint
from pathlib import Path
from typing import Dict, List


def main():
    root = Path(__file__).parent
    dirs = []
    for path in root.rglob("cookiecutter.json"):
        dirs.append(str(path).replace(str(root) + "/", ""))

    dirs = sorted(dirs)
    root_node = Node.from_path(dirs)


    with open(root / "info.json", "w") as f:
        json.dump({"dirs": dirs}, f, indent=2)



class Node:
    def __init__(self):
        self.children: Dict[str, "Node"] = {}

    @staticmethod
    def from_path(paths: List[str]) -> "Node":
        root = Node()

        for path in paths:
            current = root
            for folder in path.split("/"):
                if folder == "cookiecutter.json":
                    continue
                current = current[folder]

        return root

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def __getitem__(self, key: str) -> "Node":
        if key not in self.children:
            self.children[key] = Node()

        return self.children[key]

    def display(self, depth: int=0) -> None:
        if len(self.children) == 0:
            return

        for k, v in self.children.items():
            print(" " * depth, "-", k)
            v.display(depth=depth + 2)


if __name__ == '__main__':
    main()
