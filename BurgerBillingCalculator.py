# This program calculates final bill for a Burger Order based on a user's choice.
# Price List.
# Mini Burger (M) : $5
# Normal Burger (N): $8
# Large Burger (L) : $10
# Add Mushroom : For Mini and Normal = $1, For Large = $2
# Extra Cheese : $1
print("Welcome to Burger Shop!")
burgerSise = input("What size Burger do you want? M, N or L: ")
addMushrooms = input("Do you want Mushrooms: ")
extraCheese = input("Do you want Extra Cheese: ")
burgerPrice = 0
if burgerSise.upper == "M":
    burgerPrice = 5
elif burgerSise == "N":
    burgerPrice = 8
elif burgerSise == "L":
    burgerPrice = 10
else:
    pass
if addMushrooms == 'Y':
    if burgerSise == 'M' or burgerSise == 'N':
        burgerPrice = burgerPrice + 1
    elif burgerSise == 'l':
        burgerPrice = burgerPrice + 2
    else:
        pass
if extraCheese == 'Y':
        burgerPrice = burgerPrice + 1
else:
    pass
print(f"Your final bill is: ${burgerPrice}")

#git remote add origin https://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@github.com/Wadys/EnglishCourse