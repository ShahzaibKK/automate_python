from pathlib import Path


class ChangeNames:
    def __init__(self, path) -> None:
        self.path = Path(path)

    def change_first_prefixs(self, prefix: str):
        """Only Prefix The Name"""
        for path in self.path.iterdir():
            new_name = f"{prefix}{path.name}"
            path.rename(self.path / new_name)
            print(f"Renamed: {path} to {self.path / new_name}")


oj1 = ChangeNames(r"D:\Khuram Tiles\Main Files\Huamei Ceramics\LV")
oj1.change_first_prefixs("36LV")
