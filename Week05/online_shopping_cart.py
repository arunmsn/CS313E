"""Program to maintain an online shopping cart (Part 1)"""

# Type code for classes here
class ItemToPurchase():
    """Item to Purchase"""
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        """Prints out the name, quantity, price, and total cost"""
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity * self.item_price)}")

def main():
    """Main method"""
    print("Item 1")
    print("Enter the item name:")
    name_1 = input()
    print("Enter the item price:")
    price_1 = float(input())
    print("Enter the item quantity:")
    quantity_1 = int(input())
    item_1 = ItemToPurchase()
    item_1.item_name = name_1
    item_1.item_price = price_1
    item_1.item_quantity = quantity_1
    print()
    print("Item 2")
    print("Enter the item name:")
    name_2 = input()
    print("Enter the item price:")
    price_2 = float(input())
    print("Enter the item quantity:")
    quantity_2 = int(input())
    item_2 = ItemToPurchase()
    item_2.item_name = name_2
    item_2.item_price = price_2
    item_2.item_quantity = quantity_2
    print()

    print("TOTAL COST")
    item_1.print_item_cost()
    item_2.print_item_cost()
    print()

    print(f"Total: ${int(item_1.item_price * item_1.item_quantity + item_2.item_price * item_2.item_quantity)}")

if __name__ == "__main__":
    main()
