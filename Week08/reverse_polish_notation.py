"""reverse polish notation using a stack"""
from stack import Stack

rpn = Stack()

while True:
    input_val = input("Enter a number, symbol(+, -, /, *), or end: ")
    if input_val == "+" or input_val == "-" or input_val == "/" or input_val == "*":
        val1 = rpn.peek()
        rpn.pop()
        val2 = rpn.peek()
        rpn.pop()
        if input_val == "+":
            rpn.push(val1 + val2)
        elif input_val == "-":
            rpn.push(val1 - val2)
        elif input_val == "/":
            rpn.push(val1 / val2)
        elif input_val == "*":
            rpn.push(val1 * val2)
    elif input_val == "end":
        print(rpn)
        break
    elif input_val.isnumeric():
        rpn.push(int(input_val))
    else:
        print("Invalid input. Try again.")

"""
1 5 4 10 9 + - / +
9 + 10 = 19
19 - 4 = 15
15 / 5 = 3
3 + 1 = 4
"""