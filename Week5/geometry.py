"""geometry.py"""
import math

##################################################
###########        Point           ###############
##################################################

class Point:
    """Point class"""
    # constructor with default values
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance(self, other):
        """distance class"""
        self.dist = math.sqrt(((self.x-other.x)**2) + ((self.y-other.y)**2) + ((self.z-other.z)**2))
        return self.dist

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__(self, other):
        tol = 1.0 * (10 ** -6)
        return((abs(self.x - other.x) < tol) and \
               (abs(self.y - other.y) < tol) and \
               (abs(self.z - other.z) < tol))


##################################################
###########        Sphere          ###############
##################################################

class Sphere():
    """Sphere class"""
    # constructor with default values
    def __init__(self, x=0,y=0, z=0, radius = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(self.x, self.y, self.z)
        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return 'Center: (' + str(self.center ) + '), Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
    def surface_area(self):
        """gets the surface area"""
        self.area = math.pi * 4 * (self.radius ** 2)
        return self.area

  # compute volume of a Sphere
  # returns a floating point number
    def shape_volume(self):
        """gets the volume"""
        self.volume = math.pi * (4/3) * (self.radius ** 3)
        return self.volume

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
    def is_inside_point(self, p):
        """determines if a Point is inside the Sphere"""
        # Checks each individual dimension (x, y, z)
        if self.center.distance(p) < self.radius:
            return True
        else:
            return False

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere(self, other):
        """determines if another Sphere is inside the Sphere"""
        dist_centers = self.center.distance(other.center)
        if (dist_centers + other.radius) < self.radius:
            return True
        else:
            return False

##################################################
###########        Cube            ###############
##################################################

class Cube():
    """cube class"""
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
    def __init__(self, x = 0, y = 0, z = 0, side = 1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(self.x, self.y, self.z)
        self.side = float(side)

  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
    def __str__(self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + \
               '), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
    def surface_area(self):
        """gets the surface area"""
        self.area = 6 * (self.side ** 2)
        return self.area

  # compute volume of a Cube
  # returns a floating point number
    def shape_volume(self):
        """gets the volume"""
        self.volume = self.side ** 3
        return self.volume

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
    def is_inside_point(self, p):
        """determines if a point is inside the Cube"""
        if self.center.distance(p) < self.side / 2:
            return True
        else:
            return False

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        """determines if a Sphere is inside the Cube"""
        dist_centers = self.center.distance(a_sphere.center)
        if dist_centers + a_sphere.radius < self.side / 2:
            return True
        else:
            return False


# TODO! Here you do Test-Driven Implementation. First have the tests and then implement the methods.



# Implement this Method

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
    def is_inside_cube(self, other):
        """determines if a Cube is inside the Cube"""
        dist_centers = self.center.distance(other.center)
        if (dist_centers + other.side / 2) < self.side / 2:
            return True
        return False

# Implement this Method
# Checks if two shapes, cubes or sphere have the same volume
    def has_same_volume(self, other) -> bool:
        """checks if any two shapes have the same volume"""
        if self.shape_volume == other.shape_volume:
            return True
        return False
