import re

phone_regex = re.compile(r"\d\d\d\d(-)?\d\d\d\d\d\d\d")
mo = phone_regex.search("main Office: 0318-8811355, Marketing manager: 03168811355")
print(mo.group())


phone_regex = re.compile(r"\d\d\d\d-?\d\d\d\d\d\d\d")  # has no groups
mo = phone_regex.findall("main Office: 0318-8811355, Marketing manager: 03168811355")
print(mo)

phone_regex = re.compile(r"(\d\d\d\d)-?(\d\d\d\d\d\d\d)")  # now this has groups
mo = phone_regex.findall("main Office: 0318-8811355, Marketing manager: 03168811355")
print(mo)
