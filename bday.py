birthday = {"King": "3 Jun", "Salman": "1990", "Usman": "5584"}

while True:
    print("Enter Your Name (blank for quit)")
    name = input()
    if name == "":
        break
    if name in birthday:
        print(f"{birthday[name]} is the Bday of {name}")
    else:
        print(f"we don't have your bday record {name} but we gonna add you")
        bday = input("enter your Bday: ")
        birthday[name] = bday
        print(birthday)
