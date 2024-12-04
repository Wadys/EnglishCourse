#program determines if an entered year is a Leap Year
#Modified the leap year to be a function
import os
def leap_year(y):
    """Returns if year enered is Leap year or not"""
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return f"{y} is a Leap year"
            else:
                return f"{y} is Not a Leap Year"    
        else:
            return f"{y} is a Leap year"    
    else:
        return f"{y} is Not a Leap Year"

os.system('cls')
print("Welcome to Leap Year tester")
year = int(input("Enter Year to test: "))
print(leap_year(year))
