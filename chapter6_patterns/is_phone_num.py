# Finding Patterns of Text Without Regular Expressions
def is_phone_num(text: str):
    if len(text) != 12:
        return False
    if not text[:4].isdecimal():
        return False
    if not text[4] == "-":
        return False
    if not text[5:].isdecimal():
        return False
    return True


# phon = input("please enter your phone number using this formate 0300-00000000:")
message = "khuram tiles wholesale dealer 0318-8811355 and market one 0316-8811355"
for i in range(len(message)):
    chunk = message[i : i + 12]
    if is_phone_num(chunk):
        print(f"found phone numbers {chunk}")
print("done")
# print(is_phone_num(phon))
