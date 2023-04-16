import re

# phone_regex = re.compile(r"(\(\d\d\d\d\)) (\d\d\d\d\d\d\d)")
# mo = phone_regex.search("bro ma phone is (0315) 9749774")
# print(mo.group())

# heros_regex = re.compile(r"Batman|Superman")
# mo1 = heros_regex.search("Superman And Batman")
# mo2 = heros_regex.search("Batman And Superman")
# print(mo1.group())
# print(mo2.group())

heros_regex = re.compile(r"Super(man|a|hero)")  # Pipe Caracter |
mo = heros_regex.search("So Nehaal Naseem Loves Superhero")
print(mo.group())
print(mo.group(1))

bat_regex = re.compile(r"Bat(wo)?man")  # optional ?
mo = bat_regex.search("finally Batman beat Superman")
mo1 = bat_regex.search("time to launce Batwoman series")
print(mo.group())
print(mo1.group())

phone_regex = re.compile(r"(\(\d\d\d\d\))? (\d\d\d\d\d\d\d)")
mo = phone_regex.search("bro ma phone is (0315) 9749774")
mo1 = phone_regex.search("bro ma phone is 9749774")
print(mo.group())
print(mo1.group())

bat_regex = re.compile(r"Bat(wo)*man")  # * asterisk match zero and more
mo = bat_regex.search("finally Batman beat Superman")
mo1 = bat_regex.search("time to launce Batwoman series")
mo2 = bat_regex.search(
    "time to launce Batwowowowoman series"
)  # * asterisk match zero and more
print(mo.group())
print(mo1.group())
print(mo2.group())

bat_regex = re.compile(r"Bat(wo)+man")  # + plus match one and more
mo = bat_regex.search("finally Batman beat Superman")
mo1 = bat_regex.search("time to launce Batwoman series")
mo2 = bat_regex.search(
    "time to launce Batwowowowoman series"
)  # + plus match one and more
print(mo == None)
print(mo1.group())
print(mo2.group())


ha_regex = re.compile(r"(Ha){3,5}")
mo = ha_regex.search("HaHaHaHaHa")
mo1 = ha_regex.search("HaHa")
print(mo.group())
print(mo1 == None)

ha_regex = re.compile(r"(Ha){3,5}")  # by default greedy means find longest string
mo = ha_regex.search("HaHaHaHaHa")
print(mo.group())

ha_regex = re.compile(r"(Ha){3,5}?")  # ? non-greedy means find shortest string
mo = ha_regex.search("HaHaHaHaHa")
print(mo.group())
