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

def greeting(p_question_num):
    """Print the greeting message with the logo, taking into account the number of questions"""
    print(logo)
    print(f"There are a total of {p_question_num} Questions, you can skip a questio any tyme by typing 'skip'")
    input("press any key to get started...")

def check_answer(question_num, answer, turn, player):
    """Checks the answer validity and prins if the anwser was correct or wrong."""
    s("cls")
    correct_anwswer = quiz[question_num]["answer"]
    if correct_anwswer.lower() == answer.lower():
        print(f"Correct Answer! \n{player}'s score is {player_score[player] + 1} ")
        return True
    else:
        print(f"Wrong Answer : ( \n You have {turn -1} attempts left! \nTry Again...)")
        return False

def switch_users(p_user_index):
    """Switches players"""
    if p_user_index == 0:
        return 1
    else:
        return 0

def find_winner(player1, player2):
    """Determines which player is the winner and prints out if there is a winner or if it's a draw"""
    if player_score[player1] > player_score[player2]:
        print(f"{player1} WON! The score is {player_score[player1]}")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} WON! The score is {player_score[player2]}")
    else:
        print("IT is a DRAW!")

def print_answers():
    """Goes throught the questions and answers and prints them to be reviewed by the users"""
    for question_num, nested_dict in quiz.items():
        for question, answer in nested_dict.items():
            print(f"{question} : {answer}")

#MAIN PROGRAM
greeting(len(quiz))
players_list = input("Enter 2 players_list separated by spaces: ")
players_list = players_list.split()
player_score = dict.fromkeys(players_list,0)
current_player = players_list[0]
for question in quiz:
    print("-"*40)
    print(f"It is {current_player}'s turn")
    turns = 2
    while turns > 0:
        print(quiz[question]["question"])
        posible_answer = input("Enter Answer (To move to the next question, type 'skip') : ")
        if posible_answer == 'skip':
            break
        check = check_answer(question, posible_answer, turns, current_player)
        if check:
            player_score[current_player] += 1
            break
        turns -= 1
    current_player_index = players_list.index(current_player)
    next_player_index = switch_users(current_player_index)
    current_player = players_list[next_player_index]
find_winner(players_list[0], players_list[1])
show_correct_answer = input("Do you wnat to see correct answers? (Y/N)").lower()
if show_correct_answer == 'y':
    print_answers()    
print("Thanks for playing!")



