import re, pyperclip


phone_regex = re.compile(
    r"""(
    (\+\d\d\s\d{3})?
    (\d{4}\(\d{4}\))?  # Area Code
    (\s|-|\.)?          # Separator
    (\d{7})             # Main Number
)""",
    re.VERBOSE,
)

# mo = phone_regex.search("+92 316 9743421")
# print(mo.group())

email_regex = re.compile(
    r"""
    [a-zA-Z0-9._%+.]+    # username
    @                    # @ symble
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
""",
    re.VERBOSE,
)


text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    pass
