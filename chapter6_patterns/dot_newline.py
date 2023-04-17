import re

""" So as you guys now that . regex accept anything without newline so 
how we do that how add new """


no_new_line = re.compile(r".*")
mo = no_new_line.search("hi bro what's the problem.\n noting \nbro")
print(mo.group())

new_line = re.compile(r".*", re.DOTALL)
mo = new_line.search("hi bro what's the problem.\nnoting \nbro")
print(mo.group())
