def password_controller(p):
    if len(p) > 8:
        return True
    else:
        return False

print(password_controller("custompassword"))
