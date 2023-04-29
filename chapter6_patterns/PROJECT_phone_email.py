import re, pyperclip


phone_regex = re.compile(
    r"""(
    (\+\d{2}\s\d{3})?        # Country code
    (\d{4}|\(\d{4}\))?       # Area code
    (\s|-|\.)?               # Separator
    (\d{11}|\d{7})           # Main number
    )""",
    re.VERBOSE,
)

# mo = phone_regex.search("+92 316 9743421")
# print(mo.group())
# mo = phone_regex.findall("+92 316 9743421")
# print(mo)

email_regex = re.compile(
    r"""(
    [a-zA-Z0-9._%+.]+    # username
    @                    # @ symble
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
)""",
    re.VERBOSE,
)


text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    matches.append(groups[0].strip())
for egroups in email_regex.findall(text):
    matches.append(egroups[0].strip())

print(matches)

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied")
