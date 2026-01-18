def open_calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Select an operator (+, -, * or /): ")

    if operator == "+":
        result = num1 + num2
        print("\nAnswer: " + str(result) + "\n")
        open()
    elif operator == "-":
        result = num1 - num2
        print("\nAnswer: " + str(result) + "\n")
        open()
    elif operator == "*":
        result = num1 * num2
        print("\nAnswer: " + str(result) + "\n")
        open()
    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by 0!")
            open()
        else:
            result = num1 / num2
            print("\nAnswer: " + str(result) + "\n")
            open()

def open():
    print("Welcome to the calculator!\n")
    user_input = input("Press 'c' to contiue or press 'e' to exit: ")

    if user_input == "c":
        open_calculator()
    elif user_input == "e":
        print("Goodbye!")

open()
