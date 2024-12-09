# Create program that prints Fizz in numbers divicible by 5 Buzz in numbers divicible by 7 and
# Fizz Buzz in those divicible by both 5 and 7
for i in range(1,101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
