num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case '+':
        print("The result is ", num1 + num2)
    case '-':
        print("The result is ", num1 - num2)
    case '*':
        print("The result is ", num1 * num2)
    case '/':
        if num2 == 0:
            print("Error. Division by Zero.")
       
        print("The result is ", num1 / num2)
    case _:
        print("Error. The selected operation cannot be determined")

