'''
create a dictionary using codegnan portal as example. keys:Exams,Mock Interviews, Project Demos.
'''

# mock_CG = {
#     "Daily Exams" : ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),    #Tuple
#     "Mock Interviews with marks" : {'1st Mock Interview': 7, '2nd Mock Interview': 7},      #Dictionary
#     "Subjects" : ['Python','Aptitude','Soft Skills','MySQL'],                               #List
#     "Project Demos" : {'predictive analytics for food delivery systems','Library Management System','Inventory Management System'}, #Set
#     "Course Completion percentage" : 62.2,                                                     #Float
#     "Attendence streak" : 26,                                                                  #Int
#     "Exam Streak": 23                                                                           #Int
# }

# print(mock_CG['Course Completion percentage'])
# print(mock_CG['Mock Interviews with marks'])
# print(mock_CG['Subjects'])
# print(mock_CG['Project Demos'])
# print(mock_CG['Daily Exams'])
# print(mock_CG['Attendence streak'])
# print(mock_CG['Exam Streak'])

# Task: Use Getter and Setter methods for both Protected and Private attibutes (take a new scenario), additionally u can also have public attributes...

class Netflix:
    '''Netfilc user details'''
    def __init__(self, profile, _username, __password):
        self.profile = profile    #Public Attributes
        self._username = _username    #Protected Attributes
        self.__password = __password  #Private Attributes

    #Getter and Setter methods for Private Attribute
    def get_password(self):
        return "********"

    def set_password(self, new_password):
        if len(new_password) >= 6 and new_password.isalnum() == True:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Password length should be at least 6 characters and alphanumeric")
    
    #Getter and Setter methods for Protected Attribute
    def get_username(self):
        return self._username

    def set_username(self, new_username):
        if new_username.isalpha() == True:
            self._username = new_username
            print("Username changed successfully")
        else:
            print("Username should not contain any numbers")
    
    #Getter and Setter methods for Public Attribute
    def get_profile(self):
        return self.profile

    def set_profile(self, new_profile):
        if new_profile.isalpha() == True:
            self.profile = new_profile
            print("Profile changed successfully")
        else:
            print("Profile should not contain any numbers")

user1 = Netflix("Moviebuff","Jayakumar", "Jayakumar@2004")
print("Original Attibutes")
print(user1.get_profile())
print(user1.get_username())
print(user1.get_password())
print(user1.__dict__)
print("\nModified Attributes")
user1.set_profile("Happy")
user1.set_username("Veera")
user1.set_password("Veera2004")
print(user1.get_profile())
print(user1.get_password())
print(user1.get_username())
print(user1.__dict__)