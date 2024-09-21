"""This module is for calculating the salaries of different types of Employees and output them."""

class Employee:
    """Employee class"""
    def __init__(self, **kwargs):
        self.name = str(kwargs.get('name', ""))
        self.identifier = str(kwargs.get('identifier', ""))
        self.salary = float(kwargs.get('salary', 0))

    def __str__(self):
        return f"{self.name}, {self.identifier}, {self.salary}"

    def public_method(self):
        """This is just a filler method"""
        return 0

############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """PermanentEmployee class"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits', [])

    def cal_salary(self):
        """Calculates the salary for a Permanent Employee"""
        if self.benefits == ['health_insurance']:
            self.salary *= 0.9
        elif self.benefits == ['retirement']:
            self.salary *= 0.8
        elif self.benefits == ['retirement', 'health_insurance']:
            self.salary *= 0.7
        return self.salary

    def __str__(self):
        self.cal_salary()
        return f"{Employee.__str__(self)}, {self.benefits}"

############################################################
############################################################
############################################################

class Manager(Employee):
    """Manager class"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = float(kwargs.get('bonus', 0))

    def cal_salary(self):
        """Calculates the salary for a Manager"""
        return self.salary + self.bonus

    def __str__(self):
        """Returns a string formatted"""
        return f"{Employee.__str__(self)}, {self.bonus}"

############################################################
############################################################
############################################################

class TemporaryEmployee(Employee):
    """TemporaryEmployee class"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = float(kwargs.get('hours', 0))

    def cal_salary(self):
        """Calculates the salary for a Temporary Employee"""
        return self.salary * self.hours

    def __str__(self):
        """Prints a string formatted"""
        self.cal_salary()
        return f"{Employee.__str__(self)}, {self.hours}"

############################################################
############################################################
############################################################

class Consultant(TemporaryEmployee):
    """Consultant class"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = float(kwargs.get('travel', 0))

    def cal_salary(self):
        """Calculates the salary for a Consultant"""
        return (self.salary * self.hours) + (self.travel * 1000)

    def __str__(self):
        """Prints a string formatted"""
        self.cal_salary()
        return f"{TemporaryEmployee.__str__(self)}, {self.travel}"

############################################################
############################################################
############################################################

class ConsultantManager(Consultant, Manager):
    """ConsultantManager class"""
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.bonus = float(kwargs.get('bonus', 0))

    def cal_salary(self):
        """Calculates the salary for a Consultant Manager"""
        return (self.salary * self.hours) + (self.travel * 1000) + self.bonus

    def __str__(self):
        self.cal_salary()
        return f"{Employee.__str__(self)}, {self.hours}, {self.travel}, {self.bonus}"

############################################################
############################################################
############################################################

###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
