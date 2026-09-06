# Goal: Build a CLI Calculator with modular functions.
#Use a while True: loop, create functions for each operation, validate user input, guard against division by zero, and commit the finished project to GitHub.

def get_numbers(ask_zero_check=False):
    x = int(input("Enter your first number:"))
    y = int(input("Enter your second number:"))
            
# Simple loop that checks if y is zero
    while ask_zero_check==True and y == 0:
        y = float(input("Number should not be zero! Enter another number: "))
    return x, y


def add(x,y):
    return x+y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
        return x/y

def modulo(x,y):
        return x%y


def calculator_main():
     Calculator = True   
     while Calculator:
        print("\n--- CLI Calculator ---")
        cmd = input("Enter [A] Add, [S] Subtract, [M] Multiply, [D] Divide, [R] Modulo, or [Q] Quit: ").upper()
        match cmd:
                case "A": 
                    x,y = get_numbers()
                    print(f"The result is {add(x,y)}")
                case "S": 
                    x,y = get_numbers()
                    print(f"The result is {subtract(x,y)}")
                case "M": 
                    x,y = get_numbers()
                    print(f"The result is {multiply(x,y)}")
                case "D": 
                    x,y = get_numbers(ask_zero_check=True)
                    print(f"The result is {divide(x,y)}")
                case "R":
                    x,y = get_numbers(ask_zero_check=True)
                    print(f"The result is {modulo(x,y)}")
                case "Q": 
                        print(f"Goodbye!")
                        break
                case _:print(f"Invalid choice. Please choose a valid option.")
         
         
if __name__ == "__main__":
    calculator_main()




