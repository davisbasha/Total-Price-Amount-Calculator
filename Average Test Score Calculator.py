#Grades Assignment

#Define Constant
high_score=95
#Get test scores from users
test1=float(input("Enter the first test score: "))
test2=float(input("Enter the second test score: "))
test3=float(input("Enter the third test score: "))

#Calculate the average score
average=(test1+test2+test3)/3
#Display average score
print(f"Your average test score is: {average:.2f}")
#Congratulate the user if the average is a high score
if average > high_score:
    print("Congratulation")
    print("That is a great average!!")