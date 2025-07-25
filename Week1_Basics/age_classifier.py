# Task 1: Age Classifier
# Ask user’s age and print:
#
# “You’re a minor” if age < 18
#
# “You’re an adult” if age >= 18 and < 60
#
# “You’re a senior citizen” if age >= 60

user_age=int(input("enter your age : "))

if user_age <18:
    print("you're a minor")
elif user_age>=18 and user_age<60:
    print("you're an adult ")
else:
    print("you're a senior citizen")