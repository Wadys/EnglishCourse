##This program askes the users name, the name of the lover and then proceeds 
# to count the numbers of letters that match in "True Love" and then calculates and
# display the score
print("True Love calculator!!!")
userName =input("Enter your name: ")
loverName = input("Enter your loved one's name: ")
concat = userName.lower()+loverName.lower()
firstDigit = concat.count("t")
firstDigit += concat.count("r")
firstDigit += concat.count("u")
firstDigit += concat.count("e")
secondDigit = concat.count("l")
secondDigit += concat.count("o")
secondDigit+= concat.count("v")
secondDigit+= concat.count("e")
score = str(firstDigit)+str(secondDigit)
score = int(score)
if score < 10 or score > 85:
    print(f"Your score is {score}, you go toguether like coke and mentos.")
elif score >=40 and score <= 70: #Improved And logic
        print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")