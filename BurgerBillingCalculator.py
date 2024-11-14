# This program calculates final bill for a Burger Order based on a user's choice.
# Price List.
# Mini Burger (M) : $5
# Normal Burger (N): $8
# Large Burger (L) : $10
# Add Mushroom : For Mini and Normal = $1, For Large = $2
# Extra Cheese : $1
burgerSise = input("Please select a size for your Burger Press:\n 'M' for Mini\n 'N' for Normal\n 'L' for Large: ").upper
addMushrooms = input("Do you want to add Mushrooms to your order? 'Y'/'N': ").upper
extraCheese = input("Do you want to add Extra Cheese to your order? 'Y'/'N': ").upper
burgerPrice = 0
if burgerSise.upper == "M":
    burgerPrice = 5
elif burgerSise == "n":
    burgerPrice = 8
elif burgerSise == "l":
    burgerPrice = 10
else:
    pass
if addMushrooms == 'y':
    if burgerSise == 'm' or burgerSise == 'n':
        burgerPrice = burgerPrice + 1
    elif burgerSise == 'l':
        burgerPrice = burgerPrice + 2
    else:
        pass
if extraCheese == 'y':
        burgerPrice = burgerPrice + 1
else:
    pass
print(f"Your {burgerSise}, with mushrooms {addMushrooms} and extra cheese {extraCheese}")
print(f"Your final bill is: ${burgerPrice}")