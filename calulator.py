import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number"
    return math.sqrt(x)

def calculate():
    print("Welcome to the Calculator World!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Quit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Thank you for using the Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Enter first number: "))

            if choice != '6':
                num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))
            elif choice == '6':
                print("Result:", sqrt(num1))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculate()
