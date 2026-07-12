#Goal:
#Create functions for add, subtract, multiply, and divide. Then call them from a simple calculator menu.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operate = input("Enter [A] Add, [S] Subtract, [M] Multiply, or [D] Divide: ").upper()
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
if y == 0:
    y = int(input("The number should not be equal to zero! Enter the second number again:"))
else:
    y = int(input("Enter the second number:"))

match operate:
        case "A": 
                    print(f"The result is {add(x,y)}")
        case "S": 
                    print(f"The result is {subtract(x,y)}")
        case "M": 

                    print(f"The result is {multiply(x,y)}")
        case "D": 
                    print(f"The result is {divide(x,y)}")

