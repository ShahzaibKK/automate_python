def print_picnic_table(item: dict, lwidth, rwidth):
    print("Picnic Table".center(lwidth + rwidth, "-"))
    for k, v in item.items():
        print(f"{k.ljust(lwidth,'.')}{str(v).rjust(rwidth)}")


picnic_items = {"pizza": 20, "apple": 10, "orange": 23}
print_picnic_table(picnic_items, 12, 8)
print_picnic_table(picnic_items, 35, 40)
