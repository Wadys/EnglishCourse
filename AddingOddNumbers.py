#Implement a function that calculates the sum of all odd numbers from 
# 1 to 100 by using range() function inside loop.
import os
def add_odd_numbers():
    """Returns sum of all odd numbers from 1 to 100"""
    total = 0
    for num in range(1,100,2):
        total += num
    return total


# Implement a function which takes two parameters as start and end of 
# range and returns sum of even numbers within given range.
def add_even_numbers(start, end):
    if start % 2 != 0:
        start += 1
    suma = 0
    for n in range(start,end+1,2):
        suma += n
    return suma

#main
os.system("cls")
print(add_odd_numbers())
print(add_even_numbers(1, 100))
