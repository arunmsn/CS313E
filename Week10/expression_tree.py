"""expression_tree.py"""

#  File: ExpressionTree.py
#  Description: Working with an Expression Tree
#  Student Name: Arun Mahadevan Sathia Narayanan
#  Student UT EID: as235872
#  Course Name: CS 313E
#  Unique Number: 50184
#  Date Created: 11/04/2024
#  Date Last Modified:

import sys

OPERATORS = ['+', '-', '*', '/', '//', '%', '**']

class Stack ():
    """Stack class"""
    def __init__(self):
        self.stack = []

    def push(self, data):
        """push"""
        self.stack.append (data)

    def pop(self):
        """pop"""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        """is_empty"""
        return len(self.stack) == 0

class Node ():
    """Node class"""
    def __init__ (self, data = None, l_child = None, r_child = None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

    def get_r_child(self):
        """gets the r child"""
        return self.r_child()

    def get_l_child(self):
        """gets the l child"""
        return self.l_child()

class Tree():
    """Tree class"""
    def __init__ (self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree (self, expr):
        """creates tree"""
        elements = expr.split()
        self.root = Node()
        current = self.root
        equation = Stack()
        for token in elements:
            if token == "(":
                current.l_child = Node()
                equation.push(current)
                current = current.l_child
            elif token in OPERATORS:
                current.data = token
                equation.push(current)
                current.r_child = Node()
                current = current.r_child
            elif token == ")":
                if not equation.is_empty():
                    current = equation.pop()
            else:
                if '.' in token:
                    current.data = float(token)
                else:
                    current.data = int(token)
                if not equation.is_empty():
                    current = equation.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, a_node):
        """evaluates expressions"""
        if a_node.l_child is None and a_node.r_child is None:
            return a_node.data

        l_val = self.evaluate(a_node.l_child)
        r_val = self.evaluate(a_node.r_child)

        value = 0
        if a_node.data == '+':
            value = l_val + r_val
        if a_node.data == '-':
            value = l_val - r_val
        if a_node.data == '*':
            value = l_val * r_val
        if a_node.data == '/':
            value = l_val / r_val
        if a_node.data == '//':
            value = l_val // r_val
        if a_node.data == '%':
            value = l_val % r_val
        if a_node.data == '**':
            value = l_val ** r_val

        return float(value)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, a_node):
        """preordering of elements"""
        if a_node is None:
            return ""

        expr = str(a_node.data)
        left = self.pre_order(a_node.l_child)
        if left:
            expr += " " + left
        right = self.pre_order(a_node.r_child)
        if right:
            expr += " " + right

        return expr

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, a_node):
        """postordering of elements"""
        if a_node is None:
            return ""

        expr = ""
        left = self.post_order(a_node.l_child)
        if left:
            expr += left + " "
        right = self.post_order(a_node.r_child)
        if right:
            expr += right + " "

        expr += str(a_node.data)

        return expr

# you should NOT need to touch main, everything should be handled for you
def main():
    """main function"""
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

    # with the input being  ( ( 8 + 3 ) * ( 7 - 2 ) )
    # prefix should be      * + 8 3 - 7 2
    # postfix should be     8 3 + 7 2 - *

if __name__ == "__main__":
    main()
