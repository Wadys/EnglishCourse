##This program will greet the user and then ask for salary if the salary is over 2000 then the user is elegible for a mortgage. The program will then ask for the credit score is over 800 then the user is charged a 4% interest rate. If the credit score is lower than 800 then the user is charged a 6% interest rate.
print("Greetings this is the Mortgage Calculator!!!")
salary = float(input("What is your monthly salary? $"))
if salary >= 2000:
    print("You are eligible for a mortgage!!!")
    creditScore = int(input("What is your credit score? "))
    if creditScore > 800:
        print("Your interest rate is 4%")
    elif: 750 < creditScore and creditScore == 800
        print(f"Your interest rate is 4%")
    else:
        print("Your interest rate is 6%")
    
else:
    print("Sorry you are not eligible for a mortgage.") 
