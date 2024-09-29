"""
ADD ALL CODE BELOW THIS COMMENT
"""
from gettext import Catalog


class Item:
    def __init__(self, **kwargs):
        self.title = str(kwargs.get('title', ""))
        self.author = str(kwargs.get('author', ""))
        self.quantity = int(kwargs.get('quantity', 0))
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}")

class Borrowable:
    def __init__(self, i:Item, **kwargs):
        i.__init__(**kwargs)
        self.title = i.title
        self.author = i.author
        self.quantity = i.quantity
        self.borrowed_count = int(kwargs.get('borrowed_count', 0))

    def borrow_item(self):
        self.quantity -= 1
        self.borrowed_count += 1
        print(f"One copy of '{self.title}' has been borrowed. Remaining copies: {self.quantity}")
        if self.quantity == 0:
            print(f"All copies of {self.title} are currently borrowed.")
            return False
        return True

    def return_item(self):
        self.quantity += 1
        self.borrowed_count -= 1
        print(f"One copy of '{self.title}' has been returned. Total copies: {self.quantity}")
        if self.borrowed_count == -1:
            print(f"No copies of {self.title} are currently borrowed.")
            return False
        return True

    def is_available(self):
        return self.quantity > 0

class Book(Item, Borrowable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.isbn = str(kwargs.get('isbn', ""))

    def display_info(self):
        print(f"Book - Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}")

class DVD(Item, Borrowable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.duration = int(kwargs.get('duration', 0))

    def display_info(self):
        print(f"Book - Title: {self.title}, Author: {self.author}, Duration: {self.duration} minutes, Quantity: {self.quantity}")

class Library:
    catalog = []
    def add_item(self, i):
        self.catalog.append(i)
        print(f"Added '{i.title}' to the library catalog with quantity {i.quantity}")

    def find_item_by_title(self, title):
        for item in self.catalog:
            if item.title == title:
                return item
        print(f"'{title}' not found in library.")
        return None

    def borrow_item(self, title):
        item = self.find_item_by_title(title)
        if item:
            if isinstance(item, Borrowable):
                if item.borrow_item() == False:
                    return f"Item {item.title} cannot be borrowed."
                item.borrow_item()
            else:
                print(f"'{title}' not found in library.")

    def return_item(self, title):
        item = self.find_item_by_title(title)
        if item:
            if isinstance(item, Borrowable):
                if item.return_item() == False:
                    return f"Item {item.title} cannot be returned."
                item.return_item()
            else:
                print(f"'{title}' not found in library.")

    def list_available_items(self):
        for item in self.catalog:
            item.display_info()

# Write your input handling code here. Remember to read from stdin.
def test_library():
    library = Library()

    file = open("Exam1-OOP-SampleInput.txt", "r")
    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Check if the line describes an item (starts with 'Book' or 'DVD')
        if line.startswith("Book") or line.startswith("DVD"):
            try:
                # Parse item information: type, title, author, isbn/duration, quantity
                parts = line.split(", ")
                if line.startswith("Book") and len(parts) == 5:
                    _, title, author, isbn, quantity = parts
                    book = Book(title=title, author=author, isbn=isbn, quantity=int(quantity), borrowed_count=0)
                    library.add_item(book)
                elif line.startswith("DVD") and len(parts) == 5:
                    _, title, author, duration, quantity = parts
                    dvd = DVD(title=title, author=author, duration=int(duration), quantity=int(quantity), borrowed_count=0)
                    library.add_item(dvd)
                else:
                    raise ValueError("Invalid line in file.")
            except ValueError:
                print("Invalid line in file.")  # Invalid format in item description

        # Check if the line is a function call (starts with borrow_item, return_item, etc.)
        elif line.startswith("borrow_item:") or line.startswith("return_item:") or line == "list_available_items":
            try:
                if line.startswith("borrow_item:"):
                    title = line.split(": ")[1]
                    library.borrow_item(title)
                elif line.startswith("return_item:"):
                    title = line.split(": ")[1]
                    library.return_item(title)
                elif line == "list_available_items":
                    print("Available items in the library:")
                    for item in library.catalog:
                        if item.is_available():
                            item.display_info()
                else:
                    raise ValueError("Invalid line in file.")
            except IndexError:
                print("Invalid line in file.")  # Missing title or function parameter
        else:
            print("Invalid line in file.")  # If the line format is neither item nor function call

if __name__ == "__main__":
    test_library()
