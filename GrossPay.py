##This program will promt the user for the number of hours worked and the hourly rate, and then calculate the gross pay.
print("Welcome to gross pay calculator please provide the following data:")
hours = input("How many hours have you worked? ")
rate = input("What is your hourly rate? ")
grossPay = round(float(hours)*float(rate),2)
print(f"Your gross pay is {grossPay}")