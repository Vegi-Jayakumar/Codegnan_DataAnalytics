'''
University Management System using OOP

Classes:
    1.University
    2.Department
    3.Faculty
    4.Student
    5.Course

'''

class University:
    '''University Base Class'''
    num_colleges = 0  #Class Variable

    def __init__(self,name):
        self.name = name
        self.departments = []
        University.num_colleges += 1  #Increment class variable

    def add_department(self,department):
        self.departments.append(department)
        print(f"Department {department} is added to Departments")
    
    @classmethod
    def display_college_count(cls):
        print(f"Total number of colleges: {cls.num_colleges}")
    
class Course:
    '''Courses class'''
    def __init__(self,course_id,course_name,credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.students = []
        self.schedule = []
    
    def add_student(self,student):
        self.students.append(student)
        print(f"Student {student} is added to Course")
    
    def set_schedule(self,schedule):
        self.schedule = schedule
        print(f"Schedule for Course {self.course_name} is set to {self.schedule}")
