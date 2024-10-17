"""josephus.py"""

import sys

class Link(object):
    """Link class"""
    def __init__(self, data, next_link = None):
        self.data = data
        self.next = next_link

    def print_data(self):
        """prints the data"""
        print(self.data)

    def __str__(self):
        return str(self.data) + "-->" + str(self.next)

class CircularList(object):
    """CircularList class"""
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        """inserts an element in the list"""
        new_link = Link(data)
        current = self.first

        # if the LL is empty, then the new node itself will be the head/tail of the LL
        if current is None:
            self.first = new_link
            return

        # find the last element of the LL
        while current.next is not None:
            current = current.next

        current.next = new_link

    # Find the link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        """finds the link with the given data, or None otherwise"""
        current = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next is None:
                return None

            current = current.next

        nodes_after_current = str(current.next).split("-->")
        return nodes_after_current[0]

    # Delete a Link with the given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        """deletes a link with the given data, or None otherwise"""
        current = self.first
        previous = self.first

        if current is None:
            return None

        # keep looping until we find data to delete
        while current.data != data:
            # verify list is not empty, otherwise return None
            # also checks every node and ensures nothing is left to point to
            if current.next is None:
                return None
            # updating links in the following steps as we delete a node
            # assign the current node to the previous node
            previous = current
            # previous is the node we want, current would be the next one
            current = current.next
            # updates the current element to be the next one
        if current == self.first:
            self.first = current.next
        else:
            previous.next = current.next

        return current

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        """deletes the nth link starting from start, 
        then returns the data of the nth link and the next link"""
        pass

    # Return a string representation of a Ciruclar List
    # The format of the string will be the same as the __str__
    # format for nomal Python lists
    def __str__(self):
        pass

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code

if __name__ == "__main__":
    main()
