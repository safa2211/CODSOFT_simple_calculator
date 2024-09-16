def calculator():
    print("Simple Calculator with basic arithmetic operations")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice = input("select operations from (1/2/3/4): ")

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == '1':
        print(number1, "+", number2, "=", number1 + number2)

    elif choice == '2':
        print(number1, "-", number2, "=", number1 - number2)

    elif choice == '3':
        print(number1, "*", number2, "=", number1 * number2)

    elif choice == '4':
        if number2 != 0:
            print(number1, "/", number2, "=", number1 / number2)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice.")

calculator()
