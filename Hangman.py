# Step 1 - Picking a secret word and asking for player input
# To do list
# TODO 1 - Choose a random word from a given list which is word_list and assign it
# to variable called secret_word
# TODO 2 - Generate/show blanks which equals to number of characters in secret word
# TODO 3 - Ask a player to guess letter and assign it to a variable called guess and 
# make it upper case
import random
from os import system as s
from HangmanArt import hangman_stages
from HangmanArt import logo
def pick_word(list_p):
    '''Returns a random word from list''' 
    rando = random.randint(0,len(list_p)-1)
    word = word_list[rando]
    return word
def show_blanks(word_p):
    '''Generates show blanks which equals to number of characters in secret word'''
    blanks = len(word_p)-1
    for x in word_p:
        print('_', end= ' ')
    return blanks
def guess_letter():
    '''Ask a player to guess a letter and returns it upper cased'''
    guess = input("\nWhat letter do you choose? ")
    return guess.capitalize()

# MAIN
# secret_word = pick_word(word_list)
# print(secret_word)
# show_blanks(secret_word)
# print(guess_letter())

word_list = ['PRODUCTIVE', 'EDUCATED', 'OFFER', 'CAGEY', 'LOCK', 'WIGGLY', 'PASS', 'UNHEALTHY', 'OSSIFIED', 'BEE', 'DIFFICULT', 'LIVE', 'SNOW', 'SAFE', 'FLAME', 'WHISPER', 'OBSOLETE', 'STEP', 'USEFUL', 'CHEAP', 'LEWD', 'SPOOKY', 'BLADE', 'SUBTRACT', 'COMMON', 'DECISIVE', 'SHOE', 'EXCITING', 'PANCAKE', 'IMPARTIAL', 'SHEEP', 'NAPPY', 'AGONIZING', 'SMALL', 'MARBLE', 'HELP', 'BREATH', 'AUTOMATIC', 'LOSS', 'KITTY', 'TRUST', 'CANNON', 'PASTE', 'VOLATILE', 'MARKET', 'DROP', 'PRICEY', 'TOP', 'BRAWNY', 'REJOICE', 'JOG', 'COWS', 'PATHETIC', 'SECRET', 'PAT', 'EMPTY', 'CRAVEN', 'BLOT', 'CLASSY', 'BLOW', 'FIVE', 'STATEMENT', 'BABY', 'DIVISION', 'BOILING', 'THUNDERING', 'PROVIDE', 'MAID', 'PRESERVE', 'ASHAMED', 'STROKE', 'CROWDED', 'PIE', 'CRASH', 'GIDDY', 'SUCCEED', 'GUARDED', 'ORGANIC', 'ZEALOUS', 'TRAMP', 'CALLOUS', 'HAPPY', 'PRACTICE', 'SUCCESSFUL', 'EDUCATE', 'BOIL', 'SUDDEN', 'CAT', 'TEAM', 'COMPARISON', 'SPIKY', 'MEN', 'TIN', 'SMOGGY', 'CROWD', 'MAILBOX', 'REQUEST', 'AHEAD', 'VIVACIOUS', 'SNAKES']
secret_word = random.choice(word_list)
length_word = len(secret_word)
blank = []

for _ in range(length_word):
    blank.append('_')

guessed_letters = []
lives = 6
end_game = False
print(logo)
print(" ".join(blank))
print(hangman_stages[lives])
while not end_game:
    guess = input("Guess a letter: ").upper() 
    s('cls')
    if guess in guessed_letters:    
        print("You have already guessed this letter!")
        continue 
    else:
        guessed_letters.append(guess)
    # print(guessed_letters)

    for position in range(length_word):
        letter = secret_word[position]
        if guess == letter:
                blank[position] = letter

    if guess not in secret_word:
        lives -= 1
 
    if lives == 0:
        end_game = True
        print("You lose!")
        print(f"The word was: {secret_word}")
    print(" ".join(blank))
    print(hangman_stages[lives])
    print("Letters already tried: ", end = '')
    print(" ".join(guessed_letters))
    if "_" not in blank:
        end_game = True
        print("You win.")
    if end_game:
        ask = input("Do you want to play again? (Y/N) ").capitalize()
        if ask == "Y":
            secret_word = random.choice(word_list)
            blank.clear()
            guessed_letters.clear()
            length_word = len(secret_word)
            for _ in range(length_word):
                blank.append("_")
            end_game = False
            lives = 6
            s('cls')
            print(" ".join(blank))
            print(hangman_stages[lives])
        else:
            print("See you next time!")
            