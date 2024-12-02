# Sum of Above Average Scores
# Implement a function which takes a List as a parameter and returns the sum
# of the scores which are above average.

# Example:student_scores = [80, 60, 50, 65, 75, 55]
# sum_score_above_average(student_scores) # 220
import os
def sum_above_average(p_list):
    """Returns the sum of scores above average of a list of scores"""
    score = 0
    count = 0 
    for num in p_list:
        score += num
        count += 1
    average_score = score/count
    score = 0
    for num in p_list:
        if num > average_score:
            score += num
    return score
os.system('cls')
student_scores = [80, 60, 50, 65, 75, 55]
print(f"Sum of Above Average Scores: {sum_above_average(student_scores)}")
