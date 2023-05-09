import pyinputplus as pyip


BREAD_PRICES = {"wheat": 1.0, "white": 0.75, "sourdough": 1.25}
PROTEIN_PRICES = {"chicken": 2.0, "turkey": 1.75, "ham": 1.5, "tofu": 2.5}
CHEESE_PRICES = {"cheddar": 0.5, "Swiss": 0.75, "mozzarella": 0.6}
CONDIMENT_PRICES = {"mayo": 0.25, "mustard": 0.2, "lettuce": 0.1, "tomato": 0.2}

bread_type = pyip.inputMenu(
    ["wheat", "white", "sourdough"], prompt="Select a bread type:\n"
)
protein_type = pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], prompt="Select a protein type:\n"
)
wants_cheese = pyip.inputYesNo("Do you want cheese?\n")
if wants_cheese == "y" or "yes":
    cheese_type = pyip.inputMenu(
        ["cheddar", "Swiss", "mozzarella"], prompt="Select a cheese type:\n"
    )
    cheese_price = CHEESE_PRICES[cheese_type]
else:
    cheese_price = 0.0

wants_mayo = pyip.inputYesNo("Do you want mayo?\n")
if wants_mayo == "yes":
    mayo_price = CONDIMENT_PRICES["mayo"]
else:
    mayo_price = 0.0

wants_mustard = pyip.inputYesNo("Do you want mustard?\n")
if wants_mustard == "yes":
    mustard_price = CONDIMENT_PRICES["mustard"]
else:
    mustard_price = 0.0

wants_lettuce = pyip.inputYesNo("Do you want lettuce?\n")
if wants_lettuce == "yes":
    lettuce_price = CONDIMENT_PRICES["lettuce"]
else:
    lettuce_price = 0.0

wants_tomato = pyip.inputYesNo("Do you want tomato?\n")
if wants_tomato == "yes":
    tomato_price = CONDIMENT_PRICES["tomato"]
else:
    tomato_price = 0.0

total_sandwich = pyip.inputInt("how mana you want sir ! ", min=1)

bread_price = BREAD_PRICES[bread_type]
protein_price = PROTEIN_PRICES[protein_type]
total_cost = (
    bread_price
    + protein_price
    + cheese_price
    + mayo_price
    + mustard_price
    + lettuce_price
    + tomato_price
) * total_sandwich

print(f"your Total fucking bill has {total_cost}")
