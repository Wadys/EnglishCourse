import random
import os
os.system('cls')
while True:
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print(f"Dice1: {dice_1}")
    print(f"Dice2: {dice_2}")
    again = input("Roll the Dice again? (Y/N)") 
    if again.capitalize() == 'Y':
        continue
    elif again.capitalize() == 'N':
        break
    else:
        print("Enter a valid value")