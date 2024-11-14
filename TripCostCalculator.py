##This program will greet the user and then ask for number of days, hotel cost per night, cost of flight, cost of car rental and the cost of other expenses.
print("Greetings this is the Trip Cost Calculator!!!")
nights = float(input("How many nights will you be staying? "))
hotelCost = float(input("What is the hotel cost per night? $"))
flightCost = float(input("What is the cost of the flight? $"))
carRental = float(input("What is the cost of the car rental? $"))
otherExpenses = float(input("What are the other expenses? $"))
totalCost = round(nights*hotelCost+flightCost+carRental+otherExpenses,2)
print(f"The total cost of your trip would be: ${totalCost}")