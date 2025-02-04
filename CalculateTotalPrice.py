# Instructions:
# When program starts it will display the list of items, using available_parts dictionary
# Then program asks to select an item
# Then based on user selected item, the program checks if the item exist in the store or not. Because when quantity of 
# item is 0 then it is out of stock
# Finally, if it is not out of stock we calculate total price of items and decrease quantity from the stock. This 
# continues until user select 0. And when the loop is terminated the total price is printed to the console
from os import system as s
inventory = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}
price_quantity={
    "computer": {
        "price": 500, 
        "quantity" : 10
    },
    "monitor" : {
        "price": 200, 
        "quantity" : 8
    },
    "keyboard" : {
        "price": 500, 
        "quantity" : 5
    },
    "mouse":{
        "price": 10, 
        "quantity" : 0
    },
    "hdmi cable":{
        "price": 20, 
        "quantity" : 7

    },
    "dvd drive":{
        "price": 50, 
        "quantity" : 5
    }
}
s('cls')
total_price = 0
# Original SOlution*******************************************
# print("Please add an option from the list")
# for key, value in Inventory.items():
#     print(f"{key}: {value.capitalize()}")
# print("0: to finish")
# option = 1
# while option != 0:
#     option = int(input("> "))
#     for key, value in Inventory.items():
#         if option == key:
#             if price_quantity[value]["quantity"] == 0:
#                 print(f"{value} is out of stock!")
#             else:
#                 total_price += price_quantity[value]["price"]
#                 print(f"Adding {value}")
#                 price_quantity[value]["quantity"] -= 1 
#         elif option == 0:
#             print(f"Total price: {total_price}")
#             break
    

option = None
while option != "0":
    if option in inventory:
        value = inventory[option]
        if price_quantity[value]["quantity"] == 0:
            print(f"{value} is out of stock!")
        else:
            total_price += price_quantity[value]["price"]
            print(f"Adding {value}")
            price_quantity[value]["quantity"] -= 1
    else:
        print("Please add an option from the list")
        for key, value in inventory.items():
            print(f"{key}: {value.capitalize()}")
        print("0: to finish")
    option = input("> ")
print(f"Total price: {total_price}")