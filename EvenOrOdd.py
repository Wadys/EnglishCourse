##Prgram requires a number from the user and then prints out if the number is even or odd.
number = int(input("Type in a number: "))
if number % 2 == 0:
  print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")