# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two number
def multiplies(x, y):
    return x * y

# This function divides two numbers
def divides(x, y):
  return x / y


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1, 2, 3 or 4): ")

    #Check if choices is one of the four operation
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplies(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divides(num1, num2))
        break
    else:
        print("Invalid input")