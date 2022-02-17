from coffee_data import MENU

for coffee_type in MENU:
    if coffee_type == "espresso":
        espresso_recipe = MENU[coffee_type]["ingredients"]
        print(espresso_recipe)
