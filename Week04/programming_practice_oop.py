"""Beverage Class and Polymorphism"""

class Beverage():
    """Beverage"""
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.milk = 0
        self.sugar = 0

    def can_add_milk(self):
        """True or False"""
        pass

    def add_milk(self, units):
        """Adds the milk"""
        if self.can_add_milk() and 0 <= units <= 3:
            self.milk = units

    def add_sugar(self, units):
        """Adds the sugar"""
        if 0 <= units <= 3:
            self.sugar = units

    def get_price(self):
        """Gets the price"""
        return self.base_price

    def __str__(self):
        """Outputs a string"""
        return f"{self.name}: ${self.get_price():.2f}"

class RegularCoffee(Beverage):
    """RegularCoffee of type Beverage"""
    def __init__(self):
        """Initialization"""
        super().__init__("Regular Coffee", 1.10)

    def can_add_milk(self):
        """True or False"""
        return True

    def get_price(self):
        """Gets the price (overriden from Beverage)"""
        return self.base_price + (self.milk * 0.15) + (self.sugar * 0.10)

class Espresso(Beverage):
    """Espresso of type Beverage"""
    def __init__(self):
        """Initialization"""
        super().__init__("Espresso", 2.00)

    def can_add_milk(self):
        """True or False"""
        return True

    def get_price(self):
        """Gets the price (overriden from Beverage)"""
        return self.base_price + (self.milk * 0.15) + (self.sugar * 0.10)

class Cappuccino(Beverage):
    """Cappuccino of type Beverage"""
    def __init__(self):
        """Initialization"""
        super().__init__("Cappuccino", 3.15)

    def can_add_milk(self):
        """True or False"""
        return False

    def get_price(self):
        """Gets the price (overriden from Beverage)"""
        return self.base_price + (self.sugar * 0.10)

class CoffeeMachine:
    """CoffeeMachine"""
    def __init__(self):
        """Initialization"""
        self.beverages = {
            "1": RegularCoffee,
            "2": Espresso,
            "3": Cappuccino
        }

    def display_menu(self):
        """Displays the menu"""
        print("\nWelcome to the Coffee Machine!")
        print("1. Regular Coffee ($1.10)")
        print("2. Espresso ($2.00)")
        print("3. Cappuccino ($3.15)")
        print("4. Exit")

    def get_condiment_input(self, condiment):
        """Gets the condiments"""
        while True:
            units = input(f"How many units of {condiment} would you like? (0-3): ")
            if units.isdigit() and 0 <= int(units) <= 3:
                return int(units)
            print("Invalid input. Please enter a number between 0 and 3.")

    def brew_beverage(self):
        """Brews the Beverage"""
        while True:
            self.display_menu()
            choice = input("Please select a beverage (1-4): ")

            if choice == "4":
                print("Thank you for using the Coffee Machine. Goodbye!")
                break

            if choice not in self.beverages:
                print("Invalid choice. Please try again.")
                continue

            beverage = self.beverages[choice]()

            max_condiments = 3
            sugar_units = self.get_condiment_input("sugar")
            beverage.add_sugar(sugar_units)
            max_condiments -= sugar_units

            if beverage.can_add_milk() and max_condiments > 0:
                milk_units = self.get_condiment_input("milk")
                beverage.add_milk(milk_units)

            print(f"\nPreparing your {beverage.name}...")
            print(f"Price: ${beverage.get_price():.2f}")
            print("Enjoy your drink!")

def main():
    """Main method"""
    coffee_machine = CoffeeMachine()
    coffee_machine.brew_beverage()

if __name__ == "__main__":
    main()
