# Create a function which takes string password as a parameter and checks the length 
# of password. If the length longer than 8 character it returns True otherwise 
# returns False.
#02/12/24 Upate function to be called using a list of passwords
import os
def password_controller(p):
    """"string is verified if is over 8 char long""" #Tells what the function does
    if len(p) > 8:
        return True
    else:
        return False
#Main Programs
os.system('cls')
print(password_controller("custompassword"))
password_list = ["qwer","123456","abdcefgh","098765432"]
for pwd in password_list:
    print(pwd,password_controller(pwd))