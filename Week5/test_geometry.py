"""tests geometry.py"""
import unittest
from geometry import *


class TestGeometry(unittest.TestCase):
    """tests geometry.py"""
    def setUp(self):
        # We create a bunch of ponts first

        # The center of the coordinate system is called the origin
        self.origin = Point(0,0,0)
        self.one_above_origin = Point(0, 1, 0)
        self.one_under_origin = Point(0, -1, 0)
        self.out_point= Point(0, 1000, 0)

        self.one_radius_sphere = Sphere(0, 0, 0, 1)
        self.ten_radius_sphere = Sphere(0, -1, 0, 10)

        self.one_cube = Cube(0, 0, 0, 1)
        self.ten_cube = Cube(0, 0, 0, 10)

    def test_001_point_distance(self):
        """first test"""
        self.assertEqual(int(self.one_above_origin.distance(self.one_under_origin)), 2)
        self.assertEqual(int(self.origin.distance(self.out_point)), 1000)


# Implement the following test cases
# create objects as needed in setup or other places

    #TODO! Implement this
    def test_002_point_equality(self):
        """tests point equality"""
        # ... Implement here and remove pass
        self.assertFalse(self.one_above_origin.__eq__(self.one_under_origin),"Points are the same.")
        other_point = Point(0, 1000, 0)
        self.assertTrue(self.out_point.__eq__(other_point), "Points are not the same.")

    #TODO! Implement this
    def test_003_sphere_area(self):
        """tests sphere area"""
        self.assertTrue(self.one_radius_sphere.surface_area()
                        == 4*math.pi*(self.one_radius_sphere.radius**2),
                        "Surface Area is not calculated correctly.")
        self.assertTrue(self.ten_radius_sphere.surface_area()
                        == 4*math.pi*(self.ten_radius_sphere.radius**2),
                        "Surface Area is not calculated correctly.")

    #TODO! Implement this
    def test_004_sphere_volume(self):
        """tests sphere volume"""
        self.assertFalse(self.one_radius_sphere.shape_volume()
                         != (4/3)*math.pi*(self.one_radius_sphere.radius**3),
                         "Volume is calculated Correctly.")
        self.assertTrue(self.ten_radius_sphere.shape_volume()
                         == (4/3)*math.pi*(self.ten_radius_sphere.radius**3),
                         "Volume is calculated Correctly.")

    #TODO! Implement this
    def test_005_sphere_is_inside_point(self):
        """tests if a point is inside a sphere"""
        point_one_z = Point(0, 0, self.one_radius_sphere.radius + 1)
        point_one_y = Point(0, self.one_radius_sphere.radius + 1, 0)
        point_one_x = Point(self.one_radius_sphere.radius + 1, 0, 0)
        point_ten_z = Point(0, -1, self.ten_radius_sphere.radius - 1)
        self.assertFalse(self.one_radius_sphere.is_inside_point(point_one_z),
                         "Point is inside the sphere.")
        self.assertFalse(self.one_radius_sphere.is_inside_point(point_one_y),
                         "Point is inside the sphere.")
        self.assertFalse(self.one_radius_sphere.is_inside_point(point_one_x),
                         "Point is inside the sphere.")
        self.assertTrue(self.ten_radius_sphere.is_inside_point(point_ten_z),
                         "Point is outside or on the sphere.")        

    #TODO! Implement this
    def test_006_sphere_is_inside_sphere(self):
        """tests if a sphere is inside a sphere"""
        other_sphere_one = Sphere(0, 0, 0, 0.5)
        other_sphere_ten = Sphere(0, -1, 0, 11)
        self.assertTrue(self.one_radius_sphere.is_inside_sphere(other_sphere_one),
                        "Sphere not in Sphere.")
        self.assertFalse(self.ten_radius_sphere.is_inside_sphere(other_sphere_ten),
                         "Sphere is inside Sphere.")

   #TODO! Implement this
    def test_006_cube_is_inside_point(self):
        """tests if a point is inside a cube"""
        point_ten = Point(0, 4, 2)
        self.assertFalse(self.one_cube.is_inside_point(self.one_above_origin),
                        "Point is inside Cube.")
        self.assertTrue(self.ten_cube.is_inside_point(point_ten),
                         "Point is not inside Cube.")

   #TODO! Implement this
    def test_007_is_inside_sphere(self):
        """tests if a sphere is inside a cube"""
        sphere_ten = Sphere(0, 0, 0, 4)
        self.assertFalse(self.one_cube.is_inside_sphere(self.one_radius_sphere),
                         "Sphere is inside cube.")
        self.assertTrue(self.ten_cube.is_inside_sphere(sphere_ten),
                        "Sphere is not inside cube.")

# Here we have the test but we do not have the implementation of the method is_inside_cube()
#
# No need to change these tests here
# You need to implement the method is_inside_cube()
    def test_000_is_inside_cube(self):
        """tests if a cube is inside a cube"""
        self.assertTrue(self.one_cube.is_inside_cube(self.ten_cube))
        self.assertFalse(self.one_cube.is_inside_cube(self.one_cube))

    def test_000_has_same_volume(self):
        """tests if two shapes have the same volume"""
        self.assertTrue(self.one_cube.has_same_volume(self.one_cube))


if __name__ == '__main__':
    unittest.main()
