stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def display_inventory(stuff):
    """hello bro"""
    print("inventory:")
    total_item = 0
    for k, v in stuff.items():
        print(f"{k.title()}: {v}")
        total_item += v
    print(f"Total items you have: {total_item}")


def add_to_inventory(inv: dict, added_items):
    for item in added_items:
        inv.setdefault(item, 0)
        inv[item] += 1
    return inv


inv = {"gold coin": 42, "rope": 1}
display_inventory(inv)
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
