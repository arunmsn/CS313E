"""josephus.py"""

import sys

class Link:
    """Link class"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """gets the data"""
        return self.data

    def set_next(self, next_link):
        """sets the next link"""
        self.next = next_link

class CircularList:
    """CircularList class"""
    # Constructor
    def __init__(self):
        self.head = None

    def get_head(self):
        """gets the head of the circular list"""
        return self.head

    # Insert an element (value) in the list
    def insert(self, data):
        """inserts an element in the list"""
        new_link = Link(data)
        if not self.head:
            self.head = new_link
            new_link.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_link
            new_link.next = self.head

    # Find the link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        """finds the link with the given data, or None otherwise"""
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    # Delete a Link with the given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        """deletes a link with the given data, or None otherwise"""
        if not self.head:
            return None
        if self.head.data == data:
            if self.head.next == self.head:
                deleted = self.head
                self.head = None
                return deleted
            current = self.head
            while current.next != self.head:
                current = current.next
            deleted = self.head
            self.head = self.head.next
            current.next = self.head
            return deleted
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                deleted = current.next
                current.next = current.next.next
                return deleted
            current = current.next
        return None

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        """deletes the nth link starting from start, 
        then returns the data of the nth link and the next link"""
        if not self.head:
            return None, None
        current = start
        for _ in range(n - 1):
            current = current.next
        deleted_data = current.data
        next_start = current.next
        self.delete(current.data)
        return deleted_data, next_start

    # Return a string representation of a Ciruclar List
    # The format of the string will be the same as the __str__
    # format for nomal Python lists
    def __str__(self):
        if not self.head:
            return "[]"
        result = "["
        current = self.head
        while True:
            result += str(current.data)
            current = current.next
            if current == self.head:
                break
            result += ", "
        result += "]"
        return result

def main():
    """main function"""
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

    # Create the circular list
    circle = CircularList()
    for i in range(1, num_soldiers + 1):
        circle.insert(i)

    # Find the starting soldier
    current = circle.find(start_count)

    # Eliminate soldiers until only one remains
    while circle.head.next != circle.head:
        eliminated, current = circle.delete_after(current, elim_num)
        print(eliminated)

    # Print the last remaining soldier
    print(circle.head.data)

if __name__ == "__main__":
    main()
