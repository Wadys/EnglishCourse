# Create a function which takes string password as a parameter and checks the length 
# of password. If the length longer than 8 character it returns True otherwise 
# returns False.
def password_controller(p):
    """"string is verified if is over 8 char long""" #Tells what the function does
    if len(p) > 8:
        return True
    else:
        return False
print(password_controller("custompassword"))
