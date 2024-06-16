def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"
def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Imaginary result for square root of a negative number!"

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
choice = input("Enter choice (1/2/3/4/5/6): ")

if choice == '1':
    print("Result: ", add(num1, num2))
elif choice == '2':
    print("Result: ", subtract(num1, num2))
elif choice == '3':
    print("Result: ", multiply(num1, num2))
elif choice == '4':
    print("Result: ", divide(num1, num2))
elif choice == '5':
    print("Result: ", power(num1, num2))
elif choice == '6':
    print("Result: ", square_root(num1) if num2 == 0 else square_root(num2))
else:
    print("Invalid input")


