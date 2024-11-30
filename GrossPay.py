##This program will promt the user for the number of hours worked and the hourly rate, and then calculate the gross pay.

#15/11/24# Update program to pay any hours over 40 at 1.5 rate.
#17/11/24# UpDated program to include Try and Except so program can handle non-nimeric
#input gracefully by printing an error message and exiting the program.
#30/11/2024# Update program to separate the Eror Jandling in one function and the calculation in a separate one
import os
def check_float(p_input):
    """Returns Error if parameter is not a float"""
    try: #Updated to include TryCatch errors
        p_input = float(p_input)
        return p_input
    except ValueError: 
        return ("Error, please enter numeric input for Hours value")
        quit() 
    
def compute_pay(hours, rate):
    """Calculates gross payment calculating over time"""
    OTHours = 0
    if hours > 40:
        OTHours = hours - 40
        hours = 40   
        print(f"over time is {OTHours}")
    grossPay = round((float(hours)*float(rate))+(float(OTHours)*float(rate)*1.5),2)
    return grossPay    

os.system('cls')
print("Welcome to gross pay calculator please provide the following data:")
hours = check_float(input("How many hours have you worked? "))
rate = check_float(input("What is your hourly rate? "))
print(f"Your gross pay is {compute_pay(hours, rate)}")