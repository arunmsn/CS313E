"""Test file for todo.py"""
import unittest
from todo import LinkedList, Task, heap_push, heap_pop

class TestTodo(unittest.TestCase):
    """test class"""
    def setUp(self):
        self.tasks = LinkedList()
        self.priority_queue = []

    def test_task_creation(self):
        """Test basic task creation and attributes"""
        task = Task("Test Task", "Description", 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.status, "To Do")

    def test_linked_list_operations(self):
        """Test linked list functionality"""
        # Test insertion
        task1 = Task("Task 1", "First task", 1)
        task2 = Task("Task 2", "Second task", 2)
        self.tasks.insert(task1)
        self.tasks.insert(task2)
        self.assertEqual(len(self.tasks), 2)
        self.assertEqual(self.tasks.get(0).title, "Task 1")

        # Test removal
        removed_task = self.tasks.remove(0)
        self.assertEqual(removed_task.title, "Task 1")
        self.assertEqual(len(self.tasks), 1)

        # Test getting invalid index
        self.assertIsNone(self.tasks.get(5))

    def test_priority_queue(self):
        """Test priority queue operations"""
        # Test priority ordering
        task1 = Task("High Priority", "Important", 1)
        task2 = Task("Medium Priority", "Less important", 2)
        task3 = Task("Low Priority", "Can wait", 3)

        # Test insertion
        heap_push(self.priority_queue, task3)
        heap_push(self.priority_queue, task1)
        heap_push(self.priority_queue, task2)

        # Test that tasks come out in priority order
        self.assertEqual(heap_pop(self.priority_queue).priority, 1)
        self.assertEqual(heap_pop(self.priority_queue).priority, 2)
        self.assertEqual(heap_pop(self.priority_queue).priority, 3)

        # Test empty heap
        self.assertIsNone(heap_pop(self.priority_queue))

        # Test single element
        heap_push(self.priority_queue, task1)
        self.assertEqual(heap_pop(self.priority_queue).priority, 1)
        self.assertIsNone(heap_pop(self.priority_queue))

    def test_task_update(self):
        """Test task update functionality"""
        task = Task("Update Test", "Test description", 1)
        self.tasks.insert(task)

        # Test status update
        task.status = "In Progress"
        self.assertEqual(self.tasks.get(0).status, "In Progress")

        # Test priority update
        task.priority = 2
        self.assertEqual(self.tasks.get(0).priority, 2)

    def test_edge_cases(self):
        """Test edge cases and error conditions"""
        # Test empty list operations
        self.assertIsNone(self.tasks.remove(0))
        self.assertIsNone(self.tasks.get(0))

        # Test empty priority queue
        self.assertIsNone(heap_pop(self.priority_queue))

        # Test invalid priority value and expect a ValueError
        with self.assertRaises(ValueError):
            Task("Invalid", "Test", -1)

    def test_task_priority_validation(self):
        """Test task priority validation"""
        # Test valid priority
        task = Task("Valid Task", "Description", 1)
        self.assertEqual(task.priority, 1)

        # Test invalid priorities
        with self.assertRaises(ValueError):
            Task("Invalid Task", "Description", 0)

        with self.assertRaises(ValueError):
            Task("Invalid Task", "Description", -1)

        with self.assertRaises(ValueError):
            Task("Invalid Task", "Description", "not a number")

    def test_priority_queue_ordering(self):
        """Test priority queue maintains correct order"""
        # Create tasks with different priorities
        task1 = Task("Highest", "Description", 1)
        task2 = Task("Medium", "Description", 2)
        task3 = Task("Lowest", "Description", 3)

        # Add tasks in random order
        heap_push(self.priority_queue, task3)
        heap_push(self.priority_queue, task1)
        heap_push(self.priority_queue, task2)

        # Verify they come out in priority order
        self.assertEqual(heap_pop(self.priority_queue).title, "Highest")
        self.assertEqual(heap_pop(self.priority_queue).title, "Medium")
        self.assertEqual(heap_pop(self.priority_queue).title, "Lowest")

    def test_priority_update(self):
        """Test priority update maintains heap property"""
        task1 = Task("Task One", "Description", 2)
        task2 = Task("Task Two", "Description", 3)

        heap_push(self.priority_queue, task1)
        heap_push(self.priority_queue, task2)

        # Update priority and verify heap property
        task2.priority = 1
        # Remove and re-add to maintain heap property
        self.priority_queue.remove(task2)
        heap_push(self.priority_queue, task2)

        self.assertEqual(heap_pop(self.priority_queue).title, "Task Two")

    def test_equal_priorities(self):
        """Test handling of tasks with equal priorities"""
        task1 = Task("First", "Description", 1)
        task2 = Task("Second", "Description", 1)

        heap_push(self.priority_queue, task1)
        heap_push(self.priority_queue, task2)

        # Both tasks should have same priority
        first = heap_pop(self.priority_queue)
        second = heap_pop(self.priority_queue)
        self.assertEqual(first.priority, second.priority)

if __name__ == '__main__':
    unittest.main()
