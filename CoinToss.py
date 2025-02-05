# Write a virtual coin toss program which will randomly tell the user 
# "Heads" or "Tails".

import random
from os import system as s
from AsciiArt import cointoss_logo as logo
s('cls')
print(logo)
heads = random.randint(0,1)
if heads:
    print('> Heads')
else:
    print('> Tailes')
print()