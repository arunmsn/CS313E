import sys
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    Do not return anything, modify head in-place instead. Do not
    change the values in the list's nodes, only nodes themselves  may be changed.
    """
    if not head or not head.next:
        return
    
    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

"""
Each line in the input will consist of a list of integers separated by spaces.
Example: 1 2 3 4 5
Do not modify the code in the main method.
"""
def main():
    for line in sys.stdin:
        head = ListNode(int(line.strip().split()[0]))
        curr = head
        for val in line.strip().split()[1:]:
            curr.next = ListNode(int(val))
            curr = curr.next
        reorderList(head)
        curr = head
        while curr:
            # only print space if not the last element
            if curr.next:
                print(curr.val, end=" ")
            else:
                print(curr.val)
            curr = curr.next

if __name__ == "__main__":
    main()