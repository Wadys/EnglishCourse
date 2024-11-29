# Implement code block which asks two numbers and operation (+,-,*,/) that we want to
# perform on these numbers and returns the result.
# For example:
# -What is the first number? 2
# -What is the second number? 4
# -Pick operation from this list (+,-,*,/) *
# Output:2 * 4 = 8
import os

def calc(a,b,operator):
    """"Returns a (+, -, *, or /) b"""
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return "Error wrong operator entered"

os.system('cls')
a = int(input("What is the first number? "))
b = int(input("What is the second number? "))
operator = input("Pick operation from this list (+,-,*,/) ")
print(f"{a} {operator} {b} = {calc(a,b,operator)}")


