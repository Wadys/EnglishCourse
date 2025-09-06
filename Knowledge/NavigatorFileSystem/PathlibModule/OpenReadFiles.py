# Old way of doing it
print("Using usual method")
file = open("test.txt")
content = file.read()
print(content)
file.close()

# Same way but using with that way we don't have to worry about closing the file
print("Using with method")
with open("test.txt") as file:
    content = file.read()
    print(content)