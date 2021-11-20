import os
import shutil
from pathlib import Path

root = Path(os.path.realpath(os.path.curdir))

# Move content one directory level up.
# Content gets a tmp name to prevent conficts with dir template name.
tmp_files = []
for src in root.glob("*"):
    target = src.parents[1] / src.name
    target_tmp = src.parents[1] / (src.name + ".tmp")

    shutil.move(src, target_tmp)
    tmp_files.append((target, target_tmp))

# Remove template dir that is now empty.
shutil.rmtree(root)

# Remove tmp marker from moved files.
for target, target_tmp in tmp_files:
    os.rename(target_tmp, target)