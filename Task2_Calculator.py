#Basic Arithmetic Calculator!
#This calculator will perform calculation based on the two operands and the operator of user's choice

#function to add
def add(x, y):
    return x + y

#function to subtract
def subtract(x, y):
    return x - y

#function to multiply
def multiply(x, y):
    return x * y

#function to divide
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

#function to get the user input, compute and display the result
def calculator():
    while True:
        print("\n~~~ Simple Calculator ~~~\n")
        print("Operations:-")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit\n")

        # Get user input
        choice = input("Choose operation (enter the corresponding number or '5' to exit): ")

        if choice == '5':
            print("\nExiting the calculator. Goodbye!\n")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform calculation based on user input
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            # Display the result
            print(f"Result: {result}\n")
        else:
            print("Invalid choice. Please choose a valid operation.")

# Run the calculator
calculator()

#This calculator can perform calculations for numbers of type intrgers as well as decimals