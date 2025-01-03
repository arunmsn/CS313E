"""test_binary_tree.py"""

#  File: TestBinaryTree.py
#  Description: Program specific aspects of the Binary Tree
#  Student Name: Arun Mahadevan Sathia Narayanan
#  Student UT EID: as235872
#  Course Name: CS 313E
#  Unique Number: 50184
#  Date Created: 10/25/2024
#  Date Last Modified: 10/25/2024

import sys

class Node():
    """Node class"""
    # constructor
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """prints the node"""
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        """gets the height"""
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1

class Tree():
    """Tree class"""
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        """prints"""
        self.root.print_node(level)

    def get_height(self):
        """gets the height"""
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        """inserts the data"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        parent = self.root
        curr = self.root
        # finds location to insert new node
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        # inserts new node based on comparision to parent node
        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        return

    # Returns the range of values stored in a binary search tree of integers.
    # The range equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        """gets the range"""
        if self.root is None or self.get_height() == 1:
            return 0

        def find_min(node):
            """finds the minimum, traces to leftmost node"""
            minimum = node
            while minimum.lchild is not None:
                minimum = minimum.lchild
            return minimum.data

        def find_max(node):
            """finds the maximum, traces to rightmost node"""
            maximum = node
            while maximum.rchild is not None:
                maximum = maximum.rchild
            return maximum.data

        min_val = find_min(self.root)
        max_val = find_max(self.root)
        return max_val - min_val

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        """gets the level"""
        if self.root is None or level < 0:
            return []

        result = []
        queue = [(self.root, 0)]
        while queue:
            node, curr_level = queue.pop(0)

            # If we reach the desired level, add the node's data
            if curr_level == level:
                result.append(node)

            # Only add children to the queue if we haven't reached the desired level
            if curr_level < level:
                if node.lchild:
                    queue.append((node.lchild, curr_level + 1))
                if node.rchild:
                    queue.append((node.rchild, curr_level + 1))

        return result

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        """gets the left side view"""
        result = []

        if self.root is None:
            return result

        height = self.get_height()

        for level in range(height):
            level_nodes = self.get_level(level)

            for i, val in enumerate(level_nodes):
                level_nodes[i] = val.data

            if level_nodes:
                result.append(level_nodes[0])

        return result

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        """"sum of the leaf nodes"""
        if self.root is None:
            return 0

        def leaf_sum_helper(node):
            if node is None:
                return 0

            if node.lchild is None and node.rchild is None:
                return node.data

            return leaf_sum_helper(node.lchild) + leaf_sum_helper(node.rchild)

        return leaf_sum_helper(self.root)

def make_tree(data):
    """makes the tree"""
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

def main():
    """main method"""
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Level 0: ", t1.get_level(0))
    print("Level 1: ", t1.get_level(1))
    print("Level 2: ", t1.get_level(2))
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Level 0: ", t2.get_level(0))
    print("Level 1: ", t2.get_level(1))
    print("Level 2: ", t2.get_level(2))
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")

# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Level 0: ", t3.get_level(0))
    print("Level 1: ", t3.get_level(1))
    print("Level 2: ", t3.get_level(2))
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
