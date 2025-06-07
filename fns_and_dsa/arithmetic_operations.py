def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num1 == 0:
                print("Number should not be 0")
                return
            elif num2 == 0:
                print("Error: Division by Zero")
                return
            return num1 / num2
        case _:
            print("Unknown operation entered. Please try again")

