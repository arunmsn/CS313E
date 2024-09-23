"""Polymorphism Example"""

class Plant:
    """Plant class, Parent Class"""
    def display(self):
        """Display"""
        print("I'm a plant.")

class Mint(Plant):
    """Mint class, Child Class"""
    def display(self):
        """Display"""
        print("I'm a mint plant.")

class Lavendar(Plant):
    """Lavendar class, Child Class"""
    def display(self):
        """Display"""
        print("I'm a lavendar plant.")

plant = Mint()
plant.display()

plant = Lavendar()
plant.display()
