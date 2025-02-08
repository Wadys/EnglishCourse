# Create a program that simulates Quiz APP.
# 1. Print Logo - Quiz App
# 2. Ask for players_list and start with first player
# 3. For each questions a player can attempt two times, if first attempt is false the 
# current player can attempt second time. But if the second time the answer is incorrect 
# we switch players_list
# 4. If the answer is correct we switch players_list and the next question will be answered by 
# next player
# 5. Finally, If there is not any question left we print out winner and ask if the want to 
# see correct answers. If Yes we print the questions with answers if not we termiante the 
# program
from AsciiArt import quizapp_logo as logo
from QuizAppQA import questions_answers as quiz
from os import system as s
print(logo)
print("There are a total of 6 Questions, you can skip a questio any tyme by typing 'skip'")
input("press any key to get started...")
players_list = input("Enter 2 players_list separated by spaces: ")
players_list = players_list.split()
round = 1
player_score = dict.fromkeys(players_list,0)
current_player = players_list[0]
turns = 2
for question in quiz:
    print("-"*40)
    print(f"It is {players_list[current_player]}'s turn")
    print(quiz[round]["question"])
    posible_answer = input("Enter Answer (To move to the next question, type 'skip') : ")
    if posible_answer == quiz[round]["answer"]:
        player_score[players_list[current_player]] += 1
        s('cls')
        print("Correct Answer!")
        print(f"{players_list[current_player]}'s score is {player_score[players_list[current_player]]}")
# Switch players
    else:
        s("cls")
        print("Wrong Answer :(")
        turns -= 1
        print(f"You have {turns} turns left")
        if turns != 0:
            print("Try Again...")
    if turns == 0 or posible_answer == quiz[round]["answer"]:
        turns = 2
        if current_player == 1:
            current_player = 0
        else: 
            current_player = 1
    round +=1
print(player_score)
print_answers = input("Want to see the answers to the questions (Y/N): ")
if print_answers == 'y':
    print(quiz)
print("Thanks for playing")


