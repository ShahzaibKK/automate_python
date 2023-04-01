def pass_me_list(list):
    for i, t in enumerate(list):
        print(f"{i+1}: {t.title()}")


spam = [
    "App",
    "Bananas",
    "tofu",
    "cats",
    "apple",
]
pass_me_list(spam)
spam.sort(key=str.lower)
print(spam)
