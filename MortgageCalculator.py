##This program will greet the user and then ask for salary if the salary is over 
# 2000 then the user is elegible for a mortgage. The program will then ask for the 
# credit score is over 800 then the user is charged a 4% interest rate. If the 
# credit score is lower than 800 then the user is charged a 6% interest rate.
print("Greetings this is the Mortgage Calculator!!!")
salary = float(input("What is your monthly salary? $"))
#modifing code to include rate variable to have dinamic rate being displayed
rate = 0
if salary >= 2000:
    print("You are eligible for a mortgage!!!")
    creditScore = int(input("What is your credit score? "))
    #New logic to include rate of 3%. when creditScore between 900 and 1000 
    if creditScore >= 900 and creditScore <= 1000:
        rate = 3
    elif creditScore > 800:
        rate = 4
    elif creditScore > 750:
        rate = 6    
    else:
        rate = 8
    #updating to include Disability so that it takes 2% of any credit score if user 
    #has a disability
    disability = input("Do you have a disability y/n?")
    if disability == 'y':
        rate -= 2
    else:
        pass
    print(f"Your interest rate is {rate}%")
else:
    print("Sorry you are not eligible for a mortgage.") 

