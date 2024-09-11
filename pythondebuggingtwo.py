#input: 5 & 1; output: 5.0
#input: 10 & y; output: Not the right type! Needs to be an integer.
#input: 23 & 0; output: Can't divide by zero!
def main():
    num1 = 1
    num2 = 1
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Not the right type! Needs to be an integer.")
    try:
        if not ValueError:
            result = num1 / num2
            print(result)
            return result
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except ValueError:
        print("Not the right type! Needs to be an integer.")

main()