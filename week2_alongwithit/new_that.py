# num1=int(input("enter the num : "))
# num2=int(input("enter the num : "))
# print(type(num1+num2))
# print(type(num1-num2))
# print(type(num1*num2))
# print(type(num1/num2))


# x = 15
# y = 4
# print(x // y)
# print(x % y)
#

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
print("+","-","*","/","//","%")
operator=input("enter a operation :")
if operator == "+":
    print("result : ",num1+num2)
elif operator == "-":
    print("result : ",num1-num2)
elif operator == "*":
    print("result : ",num1 * num2)
elif operator == "/":
    print("result : ",num1/num2)
elif operator == "//":
    print("result : ",num1//num2)
elif operator == "%":
    print("result : ",num1%num2)
else:
    print("invalid answers")