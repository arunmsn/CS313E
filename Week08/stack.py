"""lesson on stacks"""
# Stacks follow a LIFO principle (Last In First Out)
# A Stack abstract data type (ADT) defines behavior
"""
push(item) - adds element to top of stack
pop() - removes element at top of stack
peek() - looks at element at top of stack
"""

"""
Stack-Empty(S)
if S.top == -1:
    return True
return False

Push(S,x)
if S.top == S.size:
    error "overflow"
else:
    S.top == S.top + 1
    S[S.top] = x

Pop(S,x)
if S.size == 0:
    error "underflow"
else:
    val = S.top
    S.top = S[S.top - 1]
    return S, val
"""
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

def main():
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push(10)
    print(my_stack)
    my_stack.push(20)
    print(my_stack)
    my_stack.push(45)
    print(my_stack)
    print("peeking:", my_stack.peek())
    print(my_stack.size())
    my_stack.pop()
    print("peeking:", my_stack.peek())
    print(my_stack.size())

if __name__ == "__main__":
    main()
