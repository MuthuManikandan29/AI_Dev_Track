def add(a, b):
    print("Result:", a + b)

def sub(a, b):
    print("Result:", a - b)

def mul(a, b):
    print("Result:", a * b)

def div(a, b):
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")

def main():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        add(a, b)
    elif op == '-':
        sub(a, b)
    elif op == '*':
        mul(a, b)
    elif op == '/':
        div(a, b)
    else:
        print("Invalid operation")

main()
