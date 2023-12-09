import re
from KINGs_work.Self_made_Program import collect_qty

for article in collect_qty().keys():
    mo_with_m = re.match(r"(\w)(?P<article_name>\d{2}\w{2}\d{3})(\w+)?(\d)?", article)

    mo_without_m = re.match(
        r"(?<!\w)(?P<article_name>\d{2}\w{2}\d{3})(\w+)?(\d)?", article
    )
    if mo_with_m:
        print(f"M....{mo_with_m.group()}")
    if mo_without_m:
        print(f"Not....{mo_without_m.group()}")
        pass
