import re
from KINGs_work.Self_made_Program import collect_qty, compress_images_path

# Assuming collect_qty() returns a dictionary
qty_dict = collect_qty()
for image in compress_images_path:
    pure = image.stem[11:]
    article_regex_pattern = rf"^{pure}(\w+)?(\d+)?$"
    article_regex = re.compile(article_regex_pattern)

    data = [["Article", "Quantity"]]
    for key in qty_dict:
        mo = article_regex.search(key)
        if mo:
            article = key
            quantity = str(qty_dict[mo.group()])
            data.append([article, quantity])
