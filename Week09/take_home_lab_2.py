#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(input_s):
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in input_s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # If it's a closing bracket
            if len(stack) == 1 or stack[-1] != bracket_map[char]:  # Check for balance
                return "NO"
            stack.pop()  # Pop the matching opening bracket

    # If stack is empty, all brackets were matched
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
