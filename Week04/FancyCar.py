FULL_TANK = 14

class FancyCar:
    def __init__(self, make = "Old Clunker", mpg = 24.0, odo = 5, tank_gauge = FULL_TANK, engine_status = False):
        # Complete the constructor.
        self.make = make
        self.mpg = mpg
        self.odo = odo
        self.tank_gauge = tank_gauge
        self.engine_status = engine_status

    # Return car model
    def get_model(self):
        # Update the return statment.
        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        return self.odo

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.
        if self.tank_gauge <= 0:
            self.tank_gauge = 0.0
            self.engine_status = False
        return self.tank_gauge

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print("The " + self.make + " says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        if miles_to_drive >= 0 and self.engine_status:
            gas_needed = miles_to_drive / self.mpg
            if gas_needed <= self.tank_gauge:
                self.tank_gauge -= gas_needed
                self.odo += miles_to_drive
            else:
                # Car runs out of gas
                miles_driven = self.tank_gauge * self.mpg
                self.odo += miles_driven
                self.tank_gauge = 0.0
            self.check_gas_gauge()
            return self.tank_gauge, self.odo
        else:
            return -1

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        if (amount_to_add >= 0 and self.engine_status is False):
            if self.tank_gauge + amount_to_add >= FULL_TANK:
                self.tank_gauge = FULL_TANK
            else:
                self.tank_gauge += amount_to_add
        else:
            self.tank_gauge = self.tank_gauge
        return self.tank_gauge

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        self.engine_status = True
        return self.engine_status

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        self.engine_status = False
        return self.engine_status

if __name__ == '__main__':
    my_car = FancyCar()
    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")
