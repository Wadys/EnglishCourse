##This is an example to show how Imports works
import math #This is a math librery that comes in Python 
import GrossPay #This is a personal library from previouse examples created by us
GrossPay.grossPay # type: ignore #This is the imported varible from Gross Pay lib the idea is to retunr a 
# warning error
result = math.pi #Imported math varible
print(result)
result = math.sqrt(16) #Imported Square Root function
print(result)

##This example request a Radious and returns the Area of a circle importing the 
# value of PI from the math library
radious = float(input("Enter Radius: "))
area = round(math.pi*radious**2,2)
print(f"The area of the circle is: {area}")

##This exmple takes advantage of the math library to calculate the factorial reult 
#from a requested number
entered = int(input("Enter a number: "))
print(f"The factorial of {entered} is: {round(math.factorial(entered),2)}")