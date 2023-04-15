import re

# phone_regex = re.compile(r"(\(\d\d\d\d\)) (\d\d\d\d\d\d\d)")
# mo = phone_regex.search("bro ma phone is (0315) 9749774")
# print(mo.group())

# heros_regex = re.compile(r"Batman|Superman")
# mo1 = heros_regex.search("Superman And Batman")
# mo2 = heros_regex.search("Batman And Superman")
# print(mo1.group())
# print(mo2.group())

heros_regex = re.compile(r"Super(man|a|hero)")
mo = heros_regex.search("So Nehaal Naseem Loves Supera")
print(mo.group())
print(mo.group(1))
