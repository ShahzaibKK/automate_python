import re


xmax = re.compile(r"\d+\s\w+")
mo = xmax.findall("0318 is 0316 not")
print(mo)

# crete my own character classes

vowel_number = re.compile(r"[aeiouAEIOU]")
mo = vowel_number.findall("i will definatly beat you, NO YOU CANT MOTER FUCKER BITCU")
print(mo)

a_z = re.compile(r"[a-zA-Z-0-9 .]")
mo = a_z.findall("King 3 .")
print(mo)


vowel_number = re.compile(
    r"[^aeiouAEIOU]"
)  # adding ^ after opening [ mean don't use this words
mo = vowel_number.findall("i will definatly beat you, NO YOU CANT MOTER FUCKER BITCU")
print(mo)
