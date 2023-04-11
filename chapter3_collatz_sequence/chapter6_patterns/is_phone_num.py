def is_phone_num(text: str):
    if not text[:3].isdecimal():
        return False
    return True


print(is_phone_num("55"))
