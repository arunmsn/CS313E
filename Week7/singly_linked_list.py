"""lesson on a singly-linked list"""

class Node():
    """Node class, with data and reference"""
    def __init__(self, data, next_link = None):
        self.data = data
        self.next = next_link

    def print_data(self):
        """prints the data"""
        print(self.data)

    def __str__(self):
        return str(self.data) + "-->" + str(self.next)

class SinglyLL():
    """Singly Linked List class, with several Nodes"""
    def __init__(self):
        self.first = None

    def insert_beginning(self, data):
        """inserting an element at the beginning of the singly linked list"""
        # create a new Node
        new_node = Node(data)

        # update the new node's next to proint to an existing node in LL
        new_node.next = self.first

        # update the head node
        self.first = new_node

    def insert_end(self, data):
        """inserting an element at the end of the singly linked list"""
        new_node = Node(data)
        current = self.first

        # if the LL is empty, then the new node itself will be the head/tail of the LL
        if current is None:
            self.first = new_node
            return

        # find the last element of the LL
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete_node(self, data):
        """removes a specified node"""
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

    def find_link(self, data):
        """find which element the current node is pointing to"""
        current = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next is None:
                return None

            current = current.next

        nodes_after_current = str(current.next).split("-->")
        current_nodes = str(current).split("-->")
        return current_nodes[0] + " points to " + nodes_after_current[0]

    def __str__(self):
        return str(self.first)

def main():
    """used to demonstrate how a singly LL works"""
    my_sll = SinglyLL()

    my_sll.insert_beginning(35)
    print(my_sll)

    my_sll.insert_beginning(33)
    print(my_sll)

    my_sll.insert_end(12)
    print(my_sll)

    my_sll.delete_node(35)
    print(my_sll)

    print(my_sll.find_link(33))

if __name__ == "__main__":
    main()
