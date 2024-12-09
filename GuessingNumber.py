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
os.system("cls")
upperB = 100
#int(input("Enter upper bound"))
lowerB = 1
#int(input("Enter lower bound"))
guess = int(input(f"Guess a number between {lowerB} and {upperB}: "))
x = random.randint(lowerB, upperB)
if x == guess:
    print("Congratulations you did it in")
elif guess > x:
    print(f"You guessed too high {guess} > {x}")
else:
    print(f"You guessed too low  {guess} < {x}")
