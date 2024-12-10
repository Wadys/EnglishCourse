# Create a function that takes two digit number from console and returns sum of digits. 
# e.g. if the input was 45, then the output should be 4 + 5 = 9
def sum_of_two_digits():
    data = input("Enter two digit number: ")
    a = int(data[0])
    b = int(data[1])
    c = a+b
    print(f"{a} + {b} = {c}")

def string_traversal(word):
#Function will print a string, each letter on a separate line.
    index = 0
    while index < len(word):
        print(word[index])
        index += 1

def string_backwardstraversal(word):
#Function will print a string starting at last character and works its way backwards to 
# the first character, printing each letter on a separate line.
    word = input("Enter a string: ")
    index = -1
    while index > -len(word)-1:
        print(word[index])
        index -= 1

def sum_word_digits(word):
#Functions take a string as parameter and return the sum of digits of a given number.
    suma = 0
    for index in range(0,len(word)):
        suma += int(word[index])
    return suma

def count_letter(word, letter):
#Count Characters in a String Implement a function count_letter that takes two parameters : a string and a letter, then returns the  number of times the letter  appears in a string
    count = 0


count_letter("Learning Python", "n")
# #Main
# sum_of_two_digits()
# string_traversal("Python")
# string_backwardstraversal("Python")
#print(sum_word_digits(input("Enter an number: ")))

