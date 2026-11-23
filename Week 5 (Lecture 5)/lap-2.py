class InvalidOperationError(Exception):
    pass

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                raise InvalidOperationError("Unsupported operation")
                
            print(f"Result: {result}")
            break
        except ValueError:
            print("Invalid numeric input.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except InvalidOperationError as e:
            print(e)
        finally:
            print("Calculation attempt completed.")

calculator()