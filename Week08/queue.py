"""lesson on queues"""
# Queues follow a FIFO principle (First In First Out)

"""
Enqueue(item) - adds element to back of queue
Dequeue(item) - remove element from back of queue
peek() - looks at element at back of queue
size() - gets the size of the queue
isEmpty() - checks if the queue is empty
"""

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

def main():
    my_queue = Queue()
    print(my_queue.is_empty())
    my_queue.enqueue(10)
    my_queue.enqueue(39)
    my_queue.enqueue(9)
    my_queue.enqueue(19)
    print(my_queue)
    my_queue.dequeue()
    print(my_queue)
    print(my_queue.peek())
    print(my_queue.size())

if __name__ == "__main__":
    main()

