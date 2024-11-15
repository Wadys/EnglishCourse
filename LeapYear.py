#program determines if an entered year is a Leap Year
print("Welcome to Leap Year tester")
year = int(input("Enter Year to test: "))
if year % 4 == 0:
    print(f"{year} is a Leap year")
else:
    print(f"{year} is Not a Leap Year")