"""
#  Description:
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:
#  Date Created:
#  Date Last Modified:
"""

import sys
import random

class Node ():
    """
    A Node of a Tree. 
    """
    def __init__ (self, data):
        """Basic Constructor """
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """
        A function to print it. 
        """
        if self.rchild is not None:
            self.rchild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.lchild is not None:
            self.lchild.print_node(level + 1)

    def __str__(self):
        """
        A simple to string method for the key.
        """
        return str(self.data)

class Tree():
    """
    A Tree Structure.
    """

    def __init__ (self):
        """Basic Constructor """
        self.root = None

    def insert(self, data):
        """
        # inserts data into l/r based on comparison with parent node        
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr is not None:
                parent = curr
                if data < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild
            # inserts new node based on comparison to parent node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    def sum_path(self, node, target):
        """
        Calculates the sum of nodes on the path from the given node to the target node.
        """
        sum_value = 0
        while node:
            sum_value += node.data
            if node.data == target:
                break
            elif target < node.data:
                node = node.lchild
            else:
                node = node.rchild
        return sum_value

    def find_lca(self, node, data_one, data_two):
        """
        Finds the Lowest Common Ancestor (LCA) of two nodes.
        """
        if node is None:
            return None
        if node.data > data_one and node.data > data_two:
            return self.find_lca(node.lchild, data_one, data_two)
        if node.data < data_one and node.data < data_two:
            return self.find_lca(node.rchild, data_one, data_two)
        return node

    def get_sum_path(self, data_one, data_two):
        """
        Calculates the sum of nodes along the path between two nodes with values 
        `data_one` and `data_two`.
        """
        lca = self.find_lca(self.root, data_one, data_two)
        if lca is None:
            return 0  # LCA not found, return 0

        sum_to_lca_from_one = self.sum_path(lca, data_one)
        sum_to_lca_from_two = self.sum_path(lca, data_two)

        # Total sum is the sum to each node minus the LCA value (to avoid double counting)
        total_sum = sum_to_lca_from_one + sum_to_lca_from_two - lca.data
        return total_sum

def main():
    """main"""
    try:
        numTests = int(input())
        num_nodes = int(input())
        tree = Tree()
        for i in range(num_nodes):
            tree.insert(int(input()))
        for i in range(numTests):
            data_one = int(input())
            data_two = int(input())
            print(tree.get_sum_path(data_one, data_two))
    except:
        pass

# python3 Q2_test_2.py < bst0.in
if __name__ == "__main__":
    main()
