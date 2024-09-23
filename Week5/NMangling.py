"""NMangling.py"""

class MyA:
    """Class MyA"""
    # this is for understanding the access of variables
    def __init__(self):
        self._var1 = "var1"
        self.__var2 = "var2"

    def get_var1(self):
        """Gets var 1"""
        return self._var1

    def get_var2(self):
        """Gets var 2"""
        return self.__var2

class MyB(MyA):
    """Class MyB"""
    def get_var1(self):
        return self._var1

    def get_var2(self):
        return self.__var2

a = MyA()
b = MyB()
print(a.get_var1(), a.get_var2())

# print(a._var1, a.__var2)
# but this print statement fails to get __var2,
# thus giving the illusion that it is private
print(a._var1) # prints out var1

print(b.get_var1(), b.get_var2())
# this also gives an error, as it is unable to access __var2
