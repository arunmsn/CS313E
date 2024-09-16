import math

class Circle:
    """Creates a circle with default dimensions or those specified by the user"""
    # self -- required in every method in the class
    # references the specific object that the method is working on
    # format for a self variable would be:
    #   self.__x = x
    # and this hides the variable x within the variable self.__x
    def __init__(self, x = 0, y = 0, rad = 0):
        self.__x = x
        self.__y = y
        self.__rad = rad

    def get_radius(self):
        """Gets radius"""
        return self.__rad

    def get_x(self):
        """Gets x"""
        return self.__x

    def get_y(self):
        """Gets y"""
        return self.__y

    def get_area(self):
        """Calculates area"""
        return math.pi * (self.__rad ** 2)

    def get_perimeter(self):
        """Calculates perimeter"""
        return 2 * math.pi * self.__rad

    def __str__(self):
        return ('x:' + str(self.__x) +
                ' y:' + str(self.__y) +
                ' radius:' + str(self.__rad))

circle1 = Circle(2, 3, 3)
circle2 = Circle(1, 2, 6)

print(circle1, 'area:', format(circle1.get_area(), ".2f"))
print(circle2, 'area:', format(circle2.get_area(), ".2f"))
