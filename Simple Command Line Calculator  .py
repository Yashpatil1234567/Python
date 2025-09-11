

def calculator():
    print("----- Simple Calculator -----")
    print("Operations: + , - , * , /")
    
    # Taking input from user
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Performing operations
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error! Division by zero is not allowed.")
            return
    else:
        print("Invalid operator!")
        return
    
    print(f"Result: {num1} {op} {num2} = {result}")


# Run the calculator
calculator()
