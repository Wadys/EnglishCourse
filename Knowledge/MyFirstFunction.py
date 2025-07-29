#This file has the  first functions

def my_first_function():
#This function  prints a welcome message
    print("Hello, I am a function")
    print("Bye for now")

def greet(name):
#This function gets a name and displayes a greeting using that name
    print(f"Hello {name}")
    print(f"How are you {name}")

def volume_converter(f_ounces):
#This function receives a volume in ounces and returs the equivelent in milliliters
    m_liters = f_ounces * 29.57353
    print(m_liters)

def greet_Name_City(name, city):
#This functions displayes a greeting using Name and city sent as parameters
    print(f"Hello {name}")
    print(f"What's the weather like in {city}")

#This part calls the functions defined above
# greet("Your Name")
# my_first_function()
# volume_converter(5)
greet_Name_City("Melany","Santa Ana")
#you can Also make the call to the function with keyword paraeters this ignores 
# the position of the parameters and is less error prone
greet_Name_City(city="Santa Ana", name="Melany") 
