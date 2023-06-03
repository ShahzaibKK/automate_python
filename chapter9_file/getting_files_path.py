from pathlib import Path
import os

p = Path(os.path.abspath("chapter9_file\getting_files_path.py"))
print(p.drive)
print(p.anchor)
print(p.parent)
print(p.parents)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.suffixes)
