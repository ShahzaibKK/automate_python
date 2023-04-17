import re


begins_with_hello = re.compile(r"^Hello")  # Mean Start From Hello
mo = begins_with_hello.search("Hello World!")
print(mo.group())

end_wit_num = re.compile(r"\d$")
mo = end_wit_num.search("my age is 27")
print(mo.group())

str_end_with_num = re.compile(r"^\d+$")
mo = str_end_with_num.search("my age is 27")
if mo == None:
    print("didt start with num")

str_end_with_num = re.compile(r"^\d+$")
mo = str_end_with_num.search("552427")
if mo == None:
    print("didt start with num")
print(mo.group())
