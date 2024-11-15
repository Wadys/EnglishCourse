##This program will promt the user for the number of hours worked and the hourly rate, and then calculate the gross pay.
print("Welcome to gross pay calculator please provide the following data:")
##Update program to pay any hours over 40 at 1.5 rate
hours = float(input("How many hours have you worked? "))
rate = input("What is your hourly rate? ")
OTHours = 0
if hours > 40:
    OTHours = hours - 40
    hours = 40   
    print(f"over time is {OTHours}")
grossPay = round((float(hours)*float(rate))+(float(OTHours)*float(rate)*1.5),2)
print(f"Your gross pay is {grossPay}")