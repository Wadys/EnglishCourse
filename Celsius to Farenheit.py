##This program will promt the user for the temperature in Celsius and the algorithim will return the temperature in Fahrenheit.
print("Welcome this is the Celsius to Fahrenheit converter!!!")
celsius = input("Enter temperature in Celsius: ")
fahrenheit = round(((float(celsius)*9/5)+32),2)
print(f"The temperature {celsius} celsius is equal to {fahrenheit} Fahrenheit")