import re

# with dot and star we enter anything dot didn't recognize newline

name = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = name.search("First Name: Shah Last Name: Zaib")
print(mo.group())


non_greedy = re.compile(r"<.*?>")
mo = non_greedy.search("<hi bro what's the problem> noting bro>")
print(mo.group())

greedy = re.compile(r"<.*>")
mo = greedy.search("<hi bro what's the problem> noting bro>")
print(mo.group())
