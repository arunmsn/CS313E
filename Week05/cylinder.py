"""the cylinder.py file"""
import math


class Cylinder:
    """creates a cylinder"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_area(self):
        """gets the area"""
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * pow(self.radius, 2))

    def get_volume(self):
        """gets the volume"""
        return math.pi * pow(self.radius, 2) * self.height

    def set_radius(self, radius):
        """sets the radius"""
        self.radius = radius

    def set_height(self, height):
        """sets the height"""
        self.height = height


# The test function to be executed by PyTest
def test_area():
    """test case area"""
    cylinder = Cylinder(5.2, 8.1)
    assert cylinder.get_area() == 434.5450958445402, "incorrect area"
    # assert cylinder.get_area() == 409, "incorrect area"

def test_volume():
    """test case volume"""
    cylinder = Cylinder(5, 8)
    assert cylinder.get_volume() == math.pi * math.pow(5, 2) * 8, "incorrect volume"
    # assert cylinder.get_volume() == 630, "incorrect volume"

#volume 688.08
test_area()
test_volume()
