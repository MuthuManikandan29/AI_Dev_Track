# Task 2: Basic Calculator
# Ask:
#
# First number
#
# Operator (+, -, *, /)
#
# Second number
#
# Perform the operation.

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
print("+","-","*","/")
operator=input("enter a operation :")
if operator =="+":
    print("result : ",num1+num2)
elif operator =="-":
    print("result : ",num1-num2)
elif operator =="*":
    print("result : ",num1 * num2)
elif operator =="/":
    print("result : ",num1/num2)
    