import pyinputplus as pyinp


while True:
    prompt = "want to know how to keep an idiot busy for hours?\n"
    response = pyinp.inputYesNo(prompt)
    if response == "no":
        break
