# Instruction
# Program will generate a password based on user inputs. Initial variables are already 
# provided.
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
# Your program should ask for number of letters, symbols and numbers initially
# Then based on these inputed values it will generate password
# Output can be like this:
# How many letters do you want in your password? 8
# How many numbers do you want in your password? 2
# How many symbols do you want in your password? 2
# Your password is: EDUpEYIG67*@
# Hint
# Use choice() function from random module to select random character from letters, nums or 
# symbols.
import random
def selections(length,list):
    pwd = ""
    for x in range(0,length):
        pwd = pwd+random.choice(list)
    return pwd
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
e_letters = int(input("How many letters do you want in your password? "))
e_nums = int(input("How many numbers do you want in your password? "))
e_symbols =int(input("How many symbols do you want in your password? "))
password = selections(e_letters,letters)+selections(e_nums,nums)+selections(e_symbols,symbols)
print(f"Your password is: {password}")

# more advances
password_list = list(password)
random.shuffle(password_list)
password = ""
for p in password_list:
    password += p
print(f"Your advanced password is: {password}")