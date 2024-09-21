class Beverage():
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.milk = 0
        self.sugar = 0

    def can_add_milk(self):
        pass

    def add_milk(self, units):
        if self.can_add_milk() and 0 <= units <= 3:
            self.milk = units

    def add_sugar(self, units):
        if 0 <= units <= 3:
            self.sugar = units

    def get_price(self):
        return self.base_price + (self.milk * 0.15) + (self.sugar * 0.10)

    def __str__(self):
        return f"{self.name}: ${self.get_price():.2f}"

class RegularCoffee(Beverage):
    def __init__(self):
        super().__init__("Regular Coffee", 1.10)

    def can_add_milk(self):
        return True

class Espresso(Beverage):
    def __init__(self):
        super().__init__("Espresso", 2.00)

    def can_add_milk(self):
        return True

class Cappuccino(Beverage):
    def __init__(self):
        super().__init__("Cappuccino", 3.15)

    def can_add_milk(self):
        return False

class CoffeeMachine:
    def __init__(self):
        self.beverages = {
            "1": RegularCoffee,
            "2": Espresso,
            "3": Cappuccino
        }

    def display_menu(self):
        print("\nWelcome to the Coffee Machine!")
        print("1. Regular Coffee ($1.10)")
        print("2. Espresso ($2.00)")
        print("3. Cappuccino ($3.15)")
        print("4. Exit")

    def get_condiment_input(self, condiment, max_units):
        while True:
            units = input(f"How many units of {condiment} would you like? (0-{max_units}): ")
            if units.isdigit() and 0 <= int(units) <= max_units:
                return int(units)
            print(f"Invalid input. Please enter a number between 0 and {max_units}.")

    def brew_beverage(self):
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
            sugar_units = self.get_condiment_input("sugar", max_condiments)
            beverage.add_sugar(sugar_units)
            max_condiments -= sugar_units

            if beverage.can_add_milk() and max_condiments > 0:
                milk_units = self.get_condiment_input("milk", max_condiments)
                beverage.add_milk(milk_units)

            print(f"\nPreparing your {beverage.name}...")
            print(f"Price: ${beverage.get_price():.2f}")
            print("Enjoy your drink!")

def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.brew_beverage()

if __name__ == "__main__":
    main()
