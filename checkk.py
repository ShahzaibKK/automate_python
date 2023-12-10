import re
from KINGs_work.Self_made_Program import collect_qty

# Assuming collect_qty() returns a dictionary
qty_dict = collect_qty()

for key, value in qty_dict.items():
    mo_with_m = re.match(r"(\w)(?P<article_name>\d{2}\w{2}\d{3})(\w+)?(\d)?", key)
    mo_without_m = re.match(r"(?<!\w)(?P<article_name>\d{2}\w{2}\d{3})(\w+)?(\d)?", key)

    if mo_with_m:
        print(f"M....{mo_with_m.group()}")
        print(f"M....{qty_dict[mo_with_m.group()]}")
