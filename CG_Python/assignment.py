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

"""
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
"""

#Task 1: Convert same to Hierarchical also make use of public, private attributes along with classmethods, class variables have functions like credit and debit within different bank classes

class RBI:
    '''Base Class'''
    cash = 10000000  #Class Variable
    #Constructor
    def __init__(self,name,_otp,__password):
        self.name = name    #Public Attribute
        self._otp = _otp    #Protected Attribute
        self.__password = __password  #Private Attribute
    #details
    def details(self):
        print(f"Name:{self.name}\nOTP:{self._otp}")
    #Get Password
    def get_password(self):
        print(f"The password is {self.__password}")
    #Class Method
    @classmethod
    def available_cash(cls):
        print("RBI has cash worth", RBI.cash)

class SBI(RBI):
    '''Derived Class(1)'''
    cash = 4000000  #Class Variable
    #Class Method
    @classmethod
    def sbi_cash(cls):
        print("SBI has cash worth",SBI.cash)
        print("Total Cash",SBI.cash + RBI.cash)

class HDFC(RBI):
    '''Derived Class(2)'''
    cash = 5000000  #Class Variable
    @classmethod
    def hdfc_cash(cls):
        print("HDFC has cash worth",HDFC.cash)
        print("Total Cash",HDFC.cash + RBI.cash)

class ICICI(RBI):
    '''Derived Class(3)'''
    cash = 5000000  #Class Variable
    @classmethod
    def icici_cash(cls):
        print("HDFC has cash worth",ICICI.cash)
        print("Total Cash",ICICI.cash + RBI.cash)

class UNION(RBI):
    '''Derived Class(3)'''
    cash = 4000000  #Class Variable
    @classmethod
    def union_cash(cls):
        print("HDFC has cash worth",UNION.cash)
        print("Total Cash",UNION.cash + RBI.cash)

class PNB(RBI):
    '''Derived Class(2)'''
    cash = 3000000  #Class Variable
    @classmethod
    def pnb_cash(cls):
        print("HDFC has cash worth",PNB.cash)
        print("Total Cash",PNB.cash + RBI.cash)

#HDFC bank
u1 = HDFC("Anuj",123654,"Anuj@123456")
u1.details()
u1.get_password()
u1.available_cash()
u1.hdfc_cash()
print(u1.__dict__)
print("\n")

#SBI bank
u2 = SBI("Babu",985632,"Babu@2011")
u2.details()
u2.get_password()
u2.available_cash()
u2.sbi_cash()
print(u2.__dict__)
print("\n")

#ICICI bank
u3 = ICICI("Charan",784521,"Charan@2006")
u3.details()
u3.get_password()
u3.available_cash()
u3.icici_cash()
print(u3.__dict__)
print("\n")

#UNION bank
u4 = UNION("Danny",451245,"Danny@2009")
u4.details()
u4.get_password()
u4.available_cash()
u4.union_cash()
print(u4.__dict__)
print("\n")

#PNB bank
u5 = PNB("Eluri",325479,"Eluri@2008")
u5.details()
u5.get_password()
u5.available_cash()
u5.pnb_cash()
print(u5.__dict__)
print("\n")

#Task2: Bring out a real time scenario for Multiple Inheritance

class Computer:
    '''Base Class(1)'''
    def keyboard(self):
        print("Keyboard is used for typing")
    
    def mouse(self):
        print("Mouse is used for clicking")
    
    def screen(self):
        print("Screen is used for displaying")

    def internet(self):
        print("device is used for surfing the internet")

class Phone:
    '''Base Class(2)'''
    def call(self):
        print("device is used for calling")
    
    def message(self):
        print("device is used for messaging")

class Camera:
    '''Base Class(3)'''
    def pic(self):
        print("This device takes pictures")

    def vid(self):
        print("This device takes videos")

class Smartphone(Computer, Phone, Camera):
    '''Derived Class'''
    def smartphone(self):
        print("Smartphone is used for all the above purposes")

#Creating an object
s1 = Smartphone()
s1.keyboard()
s1.mouse()
s1.screen()
s1.call()
s1.message()
s1.pic()
s1.vid()
s1.internet()
s1.smartphone()
