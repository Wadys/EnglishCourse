# Step 1 - Ask the player to enter first 5 numbers between 1 and 69
# To do list
# 1 - Check that the player entered 5 things 
# 2 - Convert the strings into integers
# 3 - Check that the numbers are between 1 and 69
# 4 - Check that the numbers are unique

# Step 2 - Ask the player to select the powerball between 1 to 26
# To do list
# 1 - Convert the strings into integers
# 2 - Check that the number is between 1 and 26

# Step 3 - Enter the number of times you want to play
# To do list
# 1 - Convert the strings into integers
# 2 - Check that the number is between 1 and 1000000

# Step 4 - Run the simulation
# To do list
# 1 - Come up with lottery numbers
# 2 - Display winning numbers
# 3 - Check for winner

from AsciiArt import powerball_logo as logo
from os import system as s
from random import randint as rndm 
s("cls")
print(logo)
# My solution
# def isUnique(x, p_list):
#     for n in p_list:
#         if x == n:
#             return False
#         else: 
#             pass
#     return True
# playable_five_balls = []
# s("cls")
# print(logo)
# while True:
#     playable_five_balls = []
#     input_five_balls = input("Enter 5 different numbers from 1 to 69, with spaces between each number. (For example 5 17 23 42 50)\n> ")
#     five_balls = list(input_five_balls.split())
#     if len(five_balls) == 5:
#         try:
#             for ball in five_balls:
#                 ball = int(ball)
#                 if 1 <= ball <= 69: 
#                     if isUnique(ball, five_balls):
#                         playable_five_balls.append(ball)
#                     else:
#                         print(f"Error: Ball {ball} is not Unique please try again...")
#                 else:
#                     print(f"Error: Ball {ball} is not between 1 and 69 please try again...")
#         except ValueError:
#             print(f"Value '{ball}' is not accepted. This game accepts only numbers and not text")
#         if len(playable_five_balls) == 5:
#             break
#     else:
#         print(f"You need at least 5 balls you currently have {len(five_balls)}")
# power_ball = input("Enter the powerball number from 1 to 26.\n> ")
# print(playable_five_balls)


# Course Solution

#Ask the player to enter first 5 numbers between 1 and 69
while True:
    print("Enter 5 different numbers from 1 to 69, with spaces between each number. (For example 5 17 23 42 50)")
    response = input("> ")
    numbers = response.split()
# Check that the player entered 5 things
    if len(numbers) != 5:
        print("Please enter 5 numbers, separated by spaces.")
        continue
# Convert the strings into integers
    try:
        for i in range(5):
            numbers[i] = int(numbers[i]) # type: ignore
    except ValueError:
        print(f"Please enter numbers, instead of text {numbers[i]}") # type: ignore
        continue
# Check that the numbers are between 1 and 69
    between_1_69 = True
    for  item in numbers:
        if not (1 <= item <= 69): # type: ignore
            print(f"The ball {item}, must be a number from 1 and 69")
            between_1_69 = False
            break
    if not between_1_69:
        continue
# Check that the numbers are unique
    if len(set(numbers)) != 5:
        print("You must enter 5 different numbers")
        continue
    break

# Ask the player to select the powerball between 1 to 26
while True:
    print("Enter the powerball number from 1 to 26.")
    response = input("> ")
# Convert the strings into integers
    try:
        powerball = int(response)
    except ValueError:
        print(f"Please enter numbers, instead of text")
        continue
# Check that the number is between 1 and 26
    if not (1 <= powerball <= 26):
        print("The Power ball, must be a number from 1 and 26")
        continue
    break

# Enter the number of times you want to play
while True:
    print("How many times do you want to play? (Max: 1000000)")
    response = input("> ")
# Convert the strings into integers
    try:
        playtimes = int(response)
    except ValueError:
        print(f"Please enter numbers, instead of text")
        continue
# Check that the number is between 1 and 1000000
    if not (1 <= playtimes <= 1000000):
        print("The Times you want to play, must be a number from 1 and 1000000")
        continue
    break
# Step 4 - Run the simulation
print(f"It costs ${(playtimes*2)} to play {playtimes} times, but don't worry. I'm sure you'll win it all back.")
input("Press Enter to start...")
for round in range(playtimes):
# Come up with lottery numbers
    winNumbers = set()
    while len(winNumbers) < 5:
        winNumbers.add(rndm(1,69))
    winPowerBall = rndm(1,26)
# 2 - Display winning numbers
    print(F"The winning numbers are:{winNumbers}  and {winPowerBall}", end=" ")
# 3 - Check for winner
    if(winNumbers == numbers and powerball == winPowerBall):
        print()
        print("You have won teh Powerball Lotery! Congratulations.")
        break
    else:
        print("You Lost.")
print(f"You have wasted ${(playtimes*2)}")