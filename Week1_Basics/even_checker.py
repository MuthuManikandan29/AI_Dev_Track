# Task 3: Even or Odd Checker Function
# Create a function is_even(n)
#
# Returns True if number is even
#
# Returns False if number is odd
#
# Ask the user for a number and print whether it’s even or odd.

# Task 3: Even or Odd Checker Function

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Ask the user for a number
num = int(input("Enter a number: "))

# Call the function and print result
if is_even(num):
    print("It's even")
else:
    print("It's odd")
