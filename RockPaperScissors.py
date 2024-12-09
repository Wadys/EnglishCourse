# Create a program which simulates Rock, Paper, Scissors Game Steps:
# Ask user to select rock, paper or scissors
# Then generate computer selection by using random module
# Then determine winner based on computer selection and user selection
# Finally, ask whether they want to play again or not
import os
import random
options = ["Rock","Paper","Scissors" ]
def define_winner(a, b):
    """Logic gets two parameters and defines the winner in RockPaperScissors"""
    if a == "Rock":
        if b == "Paper":
            print("Paper wraps Rock! You lose.") #Rock vs Paper = Paper
        else:
            print("Rock smashes Scissors! You win") #Rock vs Scissors = Rock
    elif a == "Paper":
        if b == "Rock": 
            print("Paper wraps Rock! You win.") #Paper vs Rock = Paper
        else:
            print("Scissors cuts Paper! You lose.") #Paper vs Scissors = Scissors
    else: 
        if b == "Paper": 
            print("Scissors cuts Paper! You win.") #Scissors vs Paper = Scissors
        else:
            print("Rock smashes Scissors! You lose") #Scissors vs Rock = Rock
while True:
    os.system("cls")
    user = input("Enter your selection:\n 1: Rock\n 2: Paper\n 3: Scissors\n")
    computer = random.choice(options)
    if user.capitalize() == computer.capitalize():
        print(f"It's a tie you chose {user.capitalize()} computer chose {computer}")
    else:
        print(f"You chose {user.capitalize()}, computer chose {computer}.")
        define_winner(user.capitalize(),computer)
    play_again = input("Play again (Y/N)? ")
    if play_again.capitalize() == 'Y':
        continue
    else:
        break