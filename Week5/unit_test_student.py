"""unit test for student (testing_code.py)"""

import unittest
from testing_code import Course, Student

class TestStudent(unittest.TestCase):
    """Tests the Student"""

    def setUp(self):
        self.cs313e = Course('cs313e', '4', '3000')
        self.cs303e = Course('cs303e', '4', '3000')

        self.course_list = [self.cs313e, self.cs303e]

        self.arun = Student("Arun", "Sathia", 2006, self.course_list)
        self.star = Student("Star", "Top", 2001, self.course_list)

    def test_generate_email_01(self):
        """tests the generate email function (01)"""
        self.assertEqual(self.arun.generate_email('utexas.edu'), 'Arun.Sathia@utexas.edu')
        # self.assertTrue('@' in list(arun.generate_email('utexas.edu')))

    def test_generate_email_02(self):
        """tests the generate email function (02)"""
        self.assertTrue('@' in list(self.arun.generate_email('utexas.edu')))

    def test_generate_email_03(self):
        """tests the generate email function (03)"""
        self.assertIn(".edu", self.star.generate_email('utexas.edu'))

if __name__ == '__main__':
    unittest.main()
