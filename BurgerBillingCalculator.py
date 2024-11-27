# This program calculates final bill for a Burger Order based on a user's choice.
# Price List.
# Mini Burger (M) : $5
# Normal Burger (N): $8
# Large Burger (L) : $10
# Add Mushroom : For Mini and Normal = $1, For Large = $2
# Extra Cheese : $1
print("Welcome to Fatboy Burger!")
burgerSise = input("Please select a size for your Burger Press:\n 'M' for Mini\n 'N' for Normal\n 'L' for Large: ").upper()
addMushrooms = input("Do you want to add Mushrooms to your order? 'Y'/'N': ").upper()
extraCheese = input("Do you want to add Extra Cheese to your order? 'Y'/'N': ").upper()
burgerPrice = 0
if burgerSise == "M":
    burgerPrice = 5
elif burgerSise == "N":
    burgerPrice = 8
elif burgerSise == "L":
    burgerPrice = 10
else:
    pass
if addMushrooms == 'Y':
    if burgerSise == 'L':
        burgerPrice += 2
    else: 
        burgerPrice += 1
if extraCheese == 'Y':
        burgerPrice += 1
print(f"Your {burgerSise}, with mushrooms {addMushrooms} and extra cheese {extraCheese}")
print(f"Your final bill is: ${burgerPrice}.")