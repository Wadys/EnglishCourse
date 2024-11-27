# We need to paint a wall and we do not know how many cans of paint we need to buy. 
# The instructions on the paint can says that 1 can of paint can cover 4 square meters
# of wall. So we need to define a function which takes as parameter  height and width 
# of wall and  calculates the area of the wall and based on the area we can calculate 
# number of cans of paint that we need.
import math
def calculate_can_number(height, width, coverage):
    print(f"{math.ceil((height*width)/coverage)}")

#print(area(2,5))
height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))
calculate_can_number(height, width, 4)
