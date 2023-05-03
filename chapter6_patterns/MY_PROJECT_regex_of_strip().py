import re


def strip_it(s, arug=None):
    if arug is None:
        pattern = r"^\s*|\s*$"
    else:
        pattern = rf"{arug}*"
    return re.sub(pattern, "", s)


print(strip_it("  i love you !  ", "love"))
