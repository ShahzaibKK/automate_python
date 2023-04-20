import re


# So regex are case sensitive which mean Robo & robo are different
# but sometime you only care of word match
# to fix this we pass second argument to re.compile, re.I or re.IGNORECASE

case_sensitive = re.compile(r"ROBOcop", re.I)
mo = case_sensitive.findall("ROBOcop ROBOCOP roBocoP")
print(mo)
