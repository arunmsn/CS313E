"""A programming example of abstraction"""
from abc import ABC, abstractmethod

class Dog(ABC):
    """The Dog Class"""
    def __init__(self, name, breed, height):
        """Initialization"""
        self.name = name
        self.breed = breed
        self.height = height

    @abstractmethod
    def print_details(self):
        """Prints out details, base version of method"""

    @abstractmethod
    def fur_type(self):
        """The Fur Type of the Dog"""

    def walk(self):
        """Because all Dogs walk."""
        print("I walk on 4 legs.")

class Poodle(Dog):
    """The Poodle Class, of type Dog"""
    def print_details(self):
        """Prints out the details"""
        print("name:", self.name, ", breed: ", self.breed, ", height: ", self.height)

    def fur_type(self):
        """Prints out the fur type"""
        print("I have curly fur")

kit = Poodle("Kit", "Poodle", "20")
kit.print_details()
kit.fur_type()
