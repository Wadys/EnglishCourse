##This program will greet the user and then ask the user for their favorite color and animal, and then print out a possible band name.
print("Welcome to the Band Name Generator.")
color = input("What is your favorite color? ")
animalName = input("What is your favorite animal? ")
print(f"Your band name could be {color.capitalize()} {animalName.capitalize()}")