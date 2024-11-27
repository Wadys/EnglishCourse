# Write a virtual coin toss program which will randomly tell the user 
# "Heads" or "Tails".

import random
heads = random.randint(0,1)
if heads:
    print('Heads')
else:
    print('Tailes')