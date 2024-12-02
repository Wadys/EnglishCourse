# Highest Score
# A List of scores of students are given, implement a program that calculates
# the highest score from the given list.
# Example:
# student_scores = [80, 60, 50, 65, 75, 55]
# The highest score in the class is: 80
import os
def high_score(list):
    """Returns the hist score from list entered as parameter"""
    h_score = 0
    for num in list:
        if h_score < num:
            h_score = num
    return h_score
#main program
os.system('cls')
student_scores = [80, 60, 50, 90, 65, 75, 55, 100]
print(f"The highst score in the class is : {high_score(student_scores)}")
