#Excamples of how to use cycles to go through a list
vegetables = ["Carrot", "Brocoli", "Corn"]
for vegetable in vegetables:
    print(vegetable)
    print(vegetable + " Pie")
print(vegetables)

#Example of using sycles to count and add
nums = [50, 90, 10]
total = 0
for num in nums:
    total += num
print(nums)
print(total)
#02/12/2024
#Using the range function you can create a list for a specific range of
#numbers you can also specify the cadance in which the numbers are skip in
#this case it's every 3rd number
for number in range(1,11,3):
    print(number)
#In this case we are adding all the numbers from 1-101
total = 0
for number in range(1,101):
    total += number
print(total)
