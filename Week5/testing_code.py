"""Just testing code out"""

class Course:
    """Course class"""
    def __init__(self, course_id, unit, tuition):
        self.course_id = course_id
        self.unit = unit
        self.tuition = tuition

class Student:
    """Student class"""
    def __init__(self, firstname, lastname, dob, course_list):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.course_list = course_list

    def generate_email(self, uni_domain):
        """Generates the email"""
        return self.firstname + "." + self.lastname + "@" + uni_domain

    def paid_tuition(self):
        """calculates the tuition"""
        tuition = 0
        for course in self.course_list:
            tuition += course.tuition
        return tuition

    def cal_discount(self, percentage):
        """calculates the discount"""
        return self.paid_tuition() * float(percentage)/100

    def get_passed_units(self):
        """gets how many units were passed"""
        return sum(course.unit for course in self.course_list)
