# Baseline code for the term project
"""The code for the ToDo Term Project"""

import os
from typing import List

class Node:
    """Defines a node"""
    def __init__(self, task):
        self.task = task
        self.next = None

class LinkedList:
    """Defines a LinkedList"""
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, task):
        """Inserts a new node at the end of the list"""
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove(self, index):
        """Removes a specified node at the index"""
        if self.head is None:
            return None
        if index == 0:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            return removed.task
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                return None
            current = current.next
        if current.next is None:
            return None
        removed = current.next
        current.next = current.next.next
        self.length -= 1
        return removed.task

    def get(self, index):
        """Gets the specific node at the index"""
        if self.head is None:
            return None
        current = self.head
        for _ in range(index):
            if current.next is None:
                return None
            current = current.next
        return current.task

    def __len__(self):
        return self.length

class Task:
    """Defines a Task with priority validation"""
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.status = "To Do"
        # Ensure priority is a positive integer
        if not isinstance(priority, int) or priority < 1:
            raise ValueError("Priority must be a positive integer (1 is highest)")
        self.priority = priority

    def __lt__(self, other):
        # Lower number means higher priority
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

def heap_push(heap, item):
    """Adds an item to the heap and then maintains the heap property"""
    heap.append(item)
    _heap_up(heap, len(heap) - 1)

def heap_pop(heap):
    """Removes an item from the heap and then maintains the heap property"""
    if not heap:
        return None

    if len(heap) == 1:
        return heap.pop()

    result = heap[0]
    heap[0] = heap.pop()  # Move last element to root
    if heap:  # Only heapify if there are elements remaining
        _heap_down(heap, 0)
    return result

def _heap_up(heap, index):
    """Maintains the heap property of the heap, bubbles up items"""
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break

def _heap_down(heap, index):
    """Maintains the heap property of the heap, bubbles down items"""
    if not heap:  # Safety check
        return

    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right

        if smallest == index:
            break

        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest

def get_user_input() -> List[str]:
    """Gets the user input with priority validation"""
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")

    while True:
        try:
            priority = int(input("Enter the task priority (1 is highest): "))
            if priority < 1:
                print("Priority must be a positive integer (1 is highest)")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    return [title, description, priority]

tasks = LinkedList()
priority_queue = []

def load_tasks():
    """Loads tasks from the file"""
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                title, description, priority, status = line.strip().split(",")
                task = Task(title, description, int(priority))
                task.status = status
                tasks.insert(task)
                heap_push(priority_queue, task)

def save_tasks():
    """Saves tasks to the file"""
    with open("todo_list.txt", "w", encoding="utf-8") as file:
        for i in range(len(tasks)):
            task = tasks.get(i)
            file.write(f"{task.title},{task.description},{task.priority},{task.status}\n")

def add_task():
    """Adds a Task with a Title, Description, and Priority"""
    title, description, priority = get_user_input()
    task = Task(title, description, priority)
    tasks.insert(task)
    heap_push(priority_queue, task)
    save_tasks()
    print(f"Added task: {title}")

def update_task():
    """Updates a Task's Status or Priority"""
    # Get the task index
    try:
        index = int(input("Enter the index of the task to update: "))
    except ValueError:
        print("Please enter a valid number")
        return

    # Verify task exists
    task = tasks.get(index-1)
    if not task:
        print("Invalid task index.")
        return

    # Show update options
    print("\nWhat would you like to update?")
    print("1. Status")
    print("2. Priority")
    update_choice = input("Enter your choice (1-2): ")

    if update_choice == "1":
        # Update status
        status = input("Enter the new status: ")
        task.status = status
        print(f"Updated task: {task.title} - Status: {status}")
    elif update_choice == "2":
        # Update priority
        try:
            new_priority = int(input("Enter the new priority (1 is highest): "))
            # Remove and re-add to priority queue to maintain heap property
            priority_queue.remove(task)
            task.priority = new_priority
            heap_push(priority_queue, task)
            print(f"Updated task: {task.title} - Priority: {new_priority}")
        except ValueError:
            print("Invalid priority value. Please enter a number.")
            return
    else:
        print("Invalid choice.")
        return

    save_tasks()

def delete_task():
    """Removes a Task at a specific index"""
    index = int(input("Enter the index of the task to delete: "))
    if tasks.get(index-1):
        task = tasks.remove(index-1)
    else:
        print("Invalid action.")
        return
    priority_queue.remove(task)
    save_tasks()
    print(f"Deleted task: {task.title}")

def list_tasks():
    """Prints out the Tasks"""
    if len(tasks) == 0:
        print("ToDo list is empty.")
    else:
        print("\nTodo List Menu:")
        print("1. View by Index")
        print("2. View by Priority")
        print("3. Filter by Status")
        choice = input("Enter your choice (1-3): ")

        # Create a list of all tasks in their current order
        task_list = []
        current = tasks.head
        while current is not None:
            task_list.append(current.task)
            current = current.next

        if choice == "1":
            print("Todo List:")
            for i, task in enumerate(task_list, 1):
                print(f"{i}. {task.title} - Status: {task.status} - Priority: {task.priority}")

        elif choice == "2":
            print("Todo List (by Priority):")
            priority_tasks = sorted(priority_queue)
            for task in priority_tasks:
                x = priority_queue.index(task)
                print(f"{x+1}. {task.title} - Status: {task.status} - Priority: {task.priority}")

        elif choice == "3":
            # Get unique statuses from existing tasks
            statuses = set(task.status for task in task_list)
            print("\nAvailable statuses:")
            for status in sorted(statuses):
                print(f"- {status}")

            # Get status to filter by
            filter_status = input("\nEnter status to filter by: ")

            # Filter and display tasks
            filtered_tasks = [task for task in task_list
                              if task.status.lower() == filter_status.lower()]

            if filtered_tasks:
                print(f"\nTasks with status '{filter_status}':")
                for i, task in enumerate(filtered_tasks, 1):
                    print(f"{i}. {task.title} - Priority: {task.priority}")
            else:
                print(f"\nNo tasks found with status '{filter_status}'")

        else:
            print("Invalid choice. Please try again.")

def main():
    """Main method"""
    load_tasks()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            save_tasks()
            print("ToDo List has been saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
