from pathlib import Path
import pyinputplus as pyinp

worng_text = Path("wrong_txt.txt")
# worng_text.write_text(
#     "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
# )
readed = worng_text.read_text()
mis_word = ["ADJECTIVE", "NOUN", "VERB"]
change_txt = ""
for word in mis_word:
    while word in readed:
        user_input = pyinp.inputStr(f"Enter word for {word.lower()}\n")
        readed = readed.replace(word, user_input, 1)

print(readed)

new_file = "new_file_correct.txt"
with open(new_file, "w") as file:
    file.write(readed)
