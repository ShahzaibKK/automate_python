from pathlib import Path
import os

print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path("bacon/foo/faltoo").is_absolute())

print(Path.cwd() / Path("checking pussy"))
print(os.path.abspath("chapter9_file\is_absolute.py"))
print(os.path.isabs("chapter9_file\is_absolute.py"))
print(os.path.relpath("D:\\", "D:\KK's/automate_python\chapter9_file\is_absolute.py"))
print(os.path.isabs(os.path.abspath(".")))
