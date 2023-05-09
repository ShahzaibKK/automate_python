import pyinputplus as pyip

# response = pyip.inputNum(">", min=5, lessThan=10, limit=2, default="N/A")
# print(response)
# response = pyip.inputNum(allowRegexes=[r"(F|U|C|K)+"])
# print(response)
response = pyip.inputNum(blockRegexes=[r"[23548]$"])
print(response)
# response = pyip.inputInt(prompt="Enter a Number")
# help(pyip.inputBool)
