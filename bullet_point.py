import pyperclip as pp

text = pp.paste()
lines = text.split("\n")
print(lines)
for i in range(len(lines)):
    lines[i] = "* " + lines[i]
    print(lines[i])

text = "\n".join(lines)
pp.copy(text)
