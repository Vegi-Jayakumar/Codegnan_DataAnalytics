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

    def __init__(self,university_name):
        self.university_name = university_name
        self.departments = []
        University.num_colleges += 1  #Increment class variable

    def add_department(self,department):
        self.departments.append(department)
        print(f"Department {department} is added to {self.university_name}")
    
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
        self.schedule = {}
    
    def add_student(self,student):
        self.students.append(student)
        print(f"Student {student.name} is added to {self.course_name} Course")
    
    def set_schedule(self,schedule):
        self.schedule = schedule

class Student:
    '''Student Class'''
    def __init__(self,student_id,name,major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.courses = []
    
    def enroll(self,course):
        self.courses.append(course)
        print(f"Student {self.name} is enrolled in {course.course_name} Course")
    
    def view_schedule(self):
        print(f"Schedule for Student {self.name}:")
        for course in self.courses:
            print(f"{course.course_id} : {course.course_name} - {course.credits}")
            for day, time in course.schedule.items():
                print(f"  {day} : {time}")
            print()

class Under_Graduate(Student):
    '''Derived class from Student class'''
    def __init__(self,student_id,name,major,gpa):
        super().__init__(student_id,name,major)
        self.gpa = gpa
    
    def view_schedule(self):
        super().view_schedule()

class Post_Graduate(Student):
    '''Derived class from Student class'''
    def __init__(self,student_id,name,major,thesis_topic):
        super().__init__(student_id,name,major)
        self.thesis_topic = thesis_topic
    
    def view_schedule(self):
        super().view_schedule()

class Department:
    '''Department Class'''
    def __init__(self,department_name,university_name):
        self.department_name = department_name
        self.university_name = university_name
        self.courses = []
    
    def add_course(self,course):
        self.courses.append(course)
        print(f"Course {course.name} is added to {self.department_name}")
    
    @staticmethod
    def get_department_type():
        print("Academic Department")

class Faculty:
    '''Faculty Class'''
    def __init__(self,faculty_id,name,course_name,department_name,university_name):
        self.faculty_id = faculty_id
        self.name = name
        self.department_name = department_name
        self.university_name = university_name
        self.course_name = course_name
        self.courses = []
    
    def assign_course(self,course):
        self.courses.append(course)
        print(f"Course {course.course_name} is assigned to {self.name}")

    def view_roaster(self):
        print(f"Student Roaster for Faculty {self.name}")
        for course in self.courses:
            print(f"\n{course.course_id} : {course.course_name}")
            for student in course.students:
                print(f"{student.student_id} : {student.name} - {student.major}")
            print()
    
    @classmethod
    def get_faculty_type(cls):
        print("Teaching Faculty")


u = University("Andhra University")
c1 = Course("CS101","Python",3)
c2 = Course("CS102","Java",3)
c3 = Course("CS103","C",3)
s = Student(101,"Jayakumar","Computer Science")
ug = Under_Graduate(201,"Abhay","Computer Science",9.0)
pg = Post_Graduate(301,"Akhil","Computer Science","AI")
f1 = Faculty(401,"Praveen","Python","Computer Science","Andhra University")
f2 = Faculty(402,"Surya","Java","Computer Science","Andhra University")
f3 = Faculty(403,"Suresh","C","Computer Science","Andhra University")
d = Department("Computer Science","Andhra University")

u.display_college_count()
print()
u.add_department("Computer Science")
print()
c1.add_student(s)
c2.add_student(ug)
c3.add_student(pg)
c1.set_schedule({"MON - SAT":"16:00 - 18:00","SUN":"HOLIDAY"})
c2.set_schedule({"MON - WED - FRI":"11:00 - 13:00","TUE - THU - SAT":"14:00 - 16:00","SUN":"HOLIDAY"})
c3.set_schedule({"TUE - THU - SAT":"14:00 - 16:00","MON - WED - FRI":"11:00 - 13:00","SUN":"HOLIDAY"})
print()
s.enroll(c1)
ug.enroll(c2)
pg.enroll(c3)
print()
s.view_schedule()
ug.view_schedule()
pg.view_schedule()
f1.assign_course(c1)
f2.assign_course(c2)
f3.assign_course(c3)
print()
f1.view_roaster()
f2.view_roaster()
f3.view_roaster()
d.get_department_type()
print()
f1.get_faculty_type()
f2.get_faculty_type()
f3.get_faculty_type()
