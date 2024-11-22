##This program will promt the user for the number of hours worked and the hourly rate, and then calculate the gross pay.
print("Welcome to gross pay calculator please provide the following data:")
#15/11/24# Update program to pay any hours over 40 at 1.5 rate.
#17/11/24# UpDated program to include Try and Except so program can handle non-nimeric
#input gracefully by printing an error message and exiting the program.
hours = input("How many hours have you worked? ")
try: #Updated to include TryCatch errors
    hours = float(hours)
except ValueError: 
    print("Error, please enter numeric input for Hours value")
    quit()
rate = input("What is your hourly rate? ")
try:
    hours = float(hours)
except ValueError:
    print("Error, please enter anumeric input for Rate value")
    quit()
OTHours = 0
if hours > 40:
    OTHours = hours - 40
    hours = 40   
    print(f"over time is {OTHours}")
grossPay = round((float(hours)*float(rate))+(float(OTHours)*float(rate)*1.5),2)
print(f"Your gross pay is {grossPay}")