from pathlib import Path
import shelve

# p = Path(r"C:/Users\shahz\Desktop/from_python.txt")
# p.write_text("its new")
# print(p.read_text())

file = open(Path.home() / "Desktop/from_python.txt", "w")
print(file.write("with Open!\n"))
file.close()
# print(file.read())
# print(Path.home())
content = open(Path.home() / "Desktop/from_python.txt")
print(content.read())

# shelf_file = shelve.open("mydata")
# cats = ["Zophie", "babu", "citty"]
# shelf_file["cats"] = cats
# shelf_file.close()

shelf_file = shelve.open("mydata")
type(shelf_file)
print(shelf_file["cats"])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
