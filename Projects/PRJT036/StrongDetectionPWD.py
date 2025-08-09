#Strong Password Checker
#Rules:
#1. The password must be at least 8 characters long.
#2. The password must include at least 1 lowercase.
#3. The password must include at least 1 uppercase.
#4. The password must include at least 1 digit.
#5. The password must include at least 1 special character.
# ## Example: strong_password_checker("k1aAawer@")
# Your password is strong!`
# # Solution:
import re
# TODO 1 - Create function which takes 1 parameter`
def strong_password_checker(password):
    # TODO 2 - Check for length of password`
    is_strong = True
    if len(password) < 8:
        print("The password must be at least 8 characters long.")
        is_strong = False
    # TODO 3 - Create regex for lowercases`
    if re.search(r'[a-z]', password) is None:
        print("The password must contain at least 1 lower  letter.")
        is_strong = False
    # TODO 4 - Create regex for uppercases`
    if re.search(r'[A-Z]', password) is None:
        print("The password must contain at least 1 upper  letter.")
        is_strong = False
    # TODO 5 - Create regex for digits`
    if re.search(r'\d', password) is None:
        print("The password must contain at least 1 digit.")
        is_strong = False
    # TODO 6 - Create regex for special characters`
    if re.search(r'[!@#$%^&*()|\\]', password) is None:
        print("The password must contain at least 1 special character.")
        is_strong = False
    # TODO 7 - If any of this returns none print message to the console` #
    if is_strong:
        print("Password is strong")

# password = input('Please enter your password: ')
strong_password_checker('aB2@5678')

