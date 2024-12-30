#Write a program for score 0.0 and 1.0 If the score is out of range, print an error
#message. If the score is in range print grade using the following table:
#Grade|Score
#  A >= 0.9
#  B >= 0.8
#  D >= 0.7
#  F  < 0.6
print("***Score Checher***")
score = input("Please enter your grade: ")
try:
    score = float(score)
except ValueError:
    print("Error, please enter a numeric input for Rate value")
    quit()
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    print(f"With a score of {score} you get a grade of {grade}")
else:
    print("Value enter is outside the range 0 to 1")

