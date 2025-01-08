# Instruction: Create a program which which asks for names and select random name from 
# the list of names. The person selected will have to pay for everybody's food bill.
# Example Input: Elshad, Edy, Redy, John, Jenny
# Example Output: Edy is going to pay for the meal today!
# Hint : Use split() function to convert string to list.
import random
import os
os.system('cls')
print(f"Type in the list of names separated by com( , ): ")
x = input("Enter a name please: ")
list = x.split(', ')
print(f"{list[random.randrange(0,len(list))]}, is going to pay for the meal today!")
