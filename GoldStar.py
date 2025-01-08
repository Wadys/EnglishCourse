# Instructions
# You are going to write a program which will automatically place the Golden STAR in a map 
# and we will find it by marking a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list 
# looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have create function to format nested list to print out like 
# this.
# ⬜️ ️⬜️ ️⬜️
# ⬜️ ️⬜️ ️⬜️
# ⬜️ ️⬜️ ️⬜️
import random
import os
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

def place_star(map1):
    x = random.randrange(0,len(map1))
    y = random.randrange(0,len(map1[x])) 
    map1[x][y] = '⭐️'
    xy = str(x+1)+str(y+1)
    return xy
os.system("cls")
map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)
coordinates = input("What do you think: Where is the Golden Star in the map? ")
xy = place_star(map1)
if xy == coordinates:
    print("Congratulations!! You have found the Golden Star!")
else:
    print("Unfortunetly you couldn't find it🤣")
    map1[int(coordinates[0])-1][int(coordinates[1])-1] = '❎'
print_map(map1)
