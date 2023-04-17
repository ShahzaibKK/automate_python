import re

dot_regex = re.compile(
    r".at"
)  # Note that . only match one character means flat become lat nad kokat become kat
mo = dot_regex.findall("cat at bat flat jat kokat")
print(mo)
