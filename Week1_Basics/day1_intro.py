# 1. Get user details
name = input("Enter your name: ")
city = input("Enter your city: ")
age = input("Enter your age: ")

print(f"Hello {name} from {city}, you are {age} years old!")

# 2. Do a simple addition
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The sum is:", num1 + num2)

# 3. Swapping variables
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swap: a =", a, ", b =", b)

# Swap logic
temp = a
a = b
b = temp

print("After swap: a =", a, ", b =", b)
