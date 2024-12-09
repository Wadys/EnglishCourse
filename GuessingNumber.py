# Create a program will generate a random number unknown to the user between upper and lower bond 
# that user provided. The user needs to guess what that number is. If the user’s guess is wrong, 
# the program should return some sort of indication as to how wrong (e.g. The number is too high 
# or too low). If the user guesses correctly, a positive indication should appear.
# Your program should ask for upper and lower bound from the user initially.
# Calculate chances of user based on upper and lower bounds.
# Based on calculated number of chances ask input from user for guessing the number.
# If the guessed number is greater than the generated number then print - "You guessed too high", 
# otherwise print - "You guessed too low". And finally if the numbers match print - 
# "Congratulations you did it in"
import random
import os
import math
os.system("cls")
lowerB = int(input("Enter lower bound: "))
upperB = int(input("Enter upper bound: "))
chance = int(math.log(upperB-lowerB+1,2))
x = random.randint(lowerB, upperB)
print(f"You've only {round(chance,0)} chances to guess the number!")
cont = 0
while cont < chance:
    cont += 1
    guess = int(input(f"Guess a number between {lowerB} and {upperB}: "))
    if x == guess:
        print(f"Congratulations you did it in {cont} try")
        break
    elif guess > x:
        print(f"You guessed too high")
    else:
        print(f"You guessed too low")
if cont == chance:
    print(f"The number is {x}") 
    print("\tBetter luck next time!")