def open_calculator():
    print("Welcome to the calculator!\n")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Select an operation (+, -, * or /): ")

    if operator == "+":
        value = num1 + num2
        print("Answer: " + str(value))
    elif operator == "-":
        value = num1 - num2
        print("Answer: " + str(value))
    elif operator == "*":
        value = num1 * num2
        print("Answer: " + str(value))
    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by 0!")
            open_calculator()
        else:
            value = num1 / num2
            print("Answer: " + str(value))

open_calculator()
