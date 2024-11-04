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

operators = ['+', '-', '*', '/', '//', '%', '**']

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
        else:
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

class Tree():
    """Tree class"""
    def __init__ (self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree (self, expr):
        """creates tree"""

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, a_node):
        """evaluates expressions"""

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, a_node):
        """preordering of elements"""

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, a_node):
        """postordering of elements"""

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
