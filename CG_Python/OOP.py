#OOP --> Object Oriented Programming

"""
OOP is a principle or paradigm which revolves around objects.

It has two main concepts:

1. Attributes (data) --> Characteristics of an object
2. Methods (functions) --> Behavior of an object. It performs the actions for the object

An object is a real world entity, whereas class is a blueprint of an object.

example:
chair --> object
Tools, Wood --> Memory
Dimensions (Blueprint) --> Class
Carpenter --> Programmer

Syntax: --> class is the keyword followed by class name(capitalized), colon and a body.

Class ClassName:
    '''Docstring'''
    #Attributes (Characteristics)
    ..........

    #Methods (Behavior)
    def methodname(self):
        ...........

a = ClassName()
b = ClassName()

or

class ClassName:
    '''Docstring'''
    def __init__(self,attribute1,attribute2,...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        ..................

    def methodname(self):
        ...................

#OOP --> Encapsulation, Inheritance, Polymorphism, Abstraction

Encapsulation: It takes one of the key properties of OOP, which bundles the data including attributes and methods into a single class.
               It provides accessibility (Public, Private, Protected) to the object's attributes and methods.

-> Public Attributes --> These are defined inside the class and can be modified outside the class.

-> Protected Attributes --> This is generally prefered in developer point of view as a hint, we generally use single underscore(_) before the attribute name. They can also be modified outside the class.

-> Private Attributes --> In this case we make the attribute name with double leading underscores(__), in vary specific cases where attribute need not be accessed directly.
                          Python breaches it by name mangling, but we prefer usage of setters and getters or accessors/modifiers

#Students class with basic details

class Students:
    '''Students class with basic details'''
    #Attributes (Characteristics)
    name = "Aakash"
    age = 21
    location = "Vizag"
    rollno = 101

    #Methods (Behaviour)
    def details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Location:",self.location)
        print("Rollno:",self.rollno)

    def study(self):
        print(f"{self.name} is studying")

#Creating an object
s1 = Students()

#Calling the methods
s1.details()
s1.study()
#print(s1.__class__)  #Returns class name (__class__) --> dunder class --> Magic Methods
#print(s1.__doc__)  #Returns class docstring
#print(s1.__dict__)  #Returns empty as we did not have constructor (Method)
#Whatever objects we create its same for all.
print("\n")
s2 = Students()
s2.name = "Veera"
s2.age = 25
s2.location = "Kakinada"
s2.rollno = 202
s2.details()
s2.study()

#In the above case we want to modify the attributes such that we can create multiple objects with specific attributes and methods.

# We will take some above example and create constructor (__init__) for the class.
# Constructor is a special type of method which is called automatically when an object is created.
# It is used to initialize the attributes of the object.

class Students:
    def __init__(self,name,age,location,rollno):
        self.name = name
        self.age = age
        self.location = location
        self.rollno = rollno

    def details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Location:",self.location)
        print("Rollno:",self.rollno)

    def study(self):
        print(f"{self.name} is studying")

#Creating an object
s1 = Students("Aakash",21,"Vizag",101)
s2 = Students("Veera",25,"Kakinada",202)

#Calling the methods
s1.details()
s1.study()
print(s1.__dict__)
print("\n")
s2.details()
s2.study()
print(s2.__dict__)

#Task: Create a cars class with attributes as brand, color, price

class Cars:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def display(self):
        print("Brand:",self.brand)
        print("Color:",self.color)
        print("Price:",self.price)

#Creating an object
c1 = Cars("Tata", "Blue", 2000000)
c2 = Cars("Mahindra", "Black", 3000000)
c3 = Cars("Toyota", "Red", 4000000)

#Calling the methods
c1.display()
print("\n")
c2.display()
print("\n")
c3.display()

class Users:
    '''Users data'''
    def __init__(self, name, _otp, __password):
        self.username = name    #Public Attributes
        self._otp = _otp        #Protected Attributes
        self.__password = __password  #Private Attributes

    def details(self):
        print("Username:",self.username)

u1 = Users("Jayakumar",5967, "Jayakumar@2004")
u1.details()
print(u1._otp)
# print(u2.__password)   #Raises AttributeError as we made it Private
print(u1._Users__password)   #here namemangling is used as we can access private attribute by classname with leading usage...
#Modifying public attribute
u1.username = "Veera"
u1.details()
#Modifying protected attribute
u1._otp = 7851  
print(u1._otp)
#Modifying private attribute
u1._Users__password = "Veera@2004" 
print(u1._Users__password)

#As NameMangling is not a recommended approach we make use of accessors and modifiers in python

class Users:
    '''Users data'''
    def __init__(self, name, _otp, __password):
        self.username = name    #Public Attributes
        self._otp = _otp        #Protected Attributes
        self.__password = __password  #Private Attributes

    #To moke use of private attributes (getter method)
    def get_password(self):
        return "********"
        # return self.__password

    #To modify the private attribute (setter method)
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Password length should be at least 6 characters")

    def details(self):
        print("Username:",self.username)
        print("OTP:",self._otp)

u2 = Users("Siva",2000,"Siva@2004")
u2.details()
print(u2.get_password())
print(u2.__dict__)
u2.set_password("sakthi@2005")   #Password length condition is satisfied
print(u2.get_password())
print(u2.__dict__)
u2.set_password("rani")   #Password length condition is not satisfied
print(u2.get_password())
print(u2.__dict__)

So we prefer usage of accessors/modifiers instead of name mangling in case of Private attributes to access and modify the data, we can use it for protected attributes too.

# Task: Use Getter and Setter methods for both Protected and Private attibutes (take a new scenario), additionally u can also have public attributes...

Inheritance: It is a mechanism in OOP where one class (child or derived class) acquires or inherits the properties (attributes and methods) of another class (parent or base class).
             Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, Hybrid Inheritance.

Syntax: 
class Base_class:  # parent class / Super class
    statements....
class Derived_Class(Base_Class):  # Child class / Sub class
    statements...

#Single Inheritance --> eg:FingurePrint
class A:
    statements...
class B(A):
    statements...

#Example of Single Inheritance: Social Media Login

class Users:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        return self.fname + " " + self.lname

class Users_v1(Users):
    pass    #This is a placeholder (Only for syntax)

class Users_v2(Users):
    def update_name(self):
        return self.fname.title().strip() + " " + self.lname.title().strip()

u1 = Users_v2("jayakumar  ","   vegi")
print(u1.full_name())
print(u1.update_name())

Using Single Inheritance we will make use of class attributes and class methods along with the importance of super() (constructor Overriding/Method Overriding)

#Banking Scenario --> Single Inheritance

class RBI:
    '''Base Class'''
    cash = 10000000  #Class Variable
    #Class Method
    @classmethod
    def available_cash(cls):
        print("RBI has cash worth", RBI.cash)

class SBI(RBI):
    '''Derived Class(1)'''
    pass

class HDFC(RBI):
    '''Derived Class(2)'''
    cash = 5000000  #Class Variable
    @classmethod
    def hdfc_cash(cls):
        print("HDFC has cash worth",HDFC.cash)
        print("Total Cash",HDFC.cash + RBI.cash)

u1 = HDFC()
u1.available_cash()
u1.hdfc_cash()

#Task 1: Convert same to Hierarchical also make use of public, private attributes along with classmethods, class variables have functions like credit and debit within different bank classes

#Kid-Father Property Scenario --> Constructor Overriding, Method Overriding

class Father:
    '''Father property interms of cash'''
    def __init__(self):
        self.property = 10000000

    def father_prop(self):
        print("Father has property worth",self.property)

class Child(Father):
    '''Child inheriting father property and having his own property'''
    def __init__(self):
        self.property = 500000
    
    def child_prop(self):
        print("Child has property worth", self.property)
        print("Total property", self.property + self.property)

obj = Child()
obj.father_prop()
obj.child_prop()

#In above we have seen constructor overriding, as we defined construtors in both base class(parent class) and derived class(child class), child class constructor has overridden the constructor of parent class.

#Constructor Overriding can be avoided by using of super() --> super().__init__() and super().__init__(args)

class Father:
    '''Father property interms of cash'''
    def __init__(self):
        self.f_property = 10000000

    def father_prop(self):
        print("Father has property worth",self.f_property)

class Child(Father):
    '''Child inheriting father property and having his own property'''
    def __init__(self):
        super().__init__()    #Calling super class constructor
        self.c_property = 500000
    
    def child_prop(self):
        print("Child has property worth", self.c_property)
        print("Total property", self.c_property + self.f_property)

obj = Child()
obj.father_prop()
obj.child_prop()

class Father:
    '''Father property interms of cash'''
    def __init__(self, f_property):
        self.f_property = f_property

    def father_prop(self):
        print("Father has property worth",self.f_property)

class Child(Father):
    '''Child inheriting father property and having his own property'''
    def __init__(self,f_property,c_property):
        super().__init__(f_property)    #Calling Super class Constructor with arguments
        self.c_property = c_property
    
    def child_prop(self):
        print("Child has property worth", self.c_property)
        print("Total property", self.c_property + self.f_property)

obj = Child(10000000,500000)
obj.father_prop()
obj.child_prop()

#Method Overriding --> When we define same method same in parent class and also in child class, it will result in Method Overriding, to get rid of this we prefer super().method()

class Square:
    '''Base class'''
    def __init__(self,x):
        self.side = x
    
    def area(self):
        print(f"Area of Square with side {self.side}: {self.side * self.side}")

class Rectangle(Square):
    '''Derived Class(1)'''
    def __init__(self,x,y):
        super().__init__(x)   #Calling Super class constructor
        self.length = y
    
    def area(self):
        super().area()  # Calling Super class method
        print(f"Area of Rectangle with length {self.length} and breadth {self.side}: {self.side * self.length}")

x,y = map(int, input("Enter digits: ").split())
a1 = Rectangle(x,y)
a1.area()

#Method Overriding will only happen with Inheritance usage

#Multiple Inheritance --> One derived class acquiring properites from two or more base classes
#Parent (Father, Mother) --> Child

Syntax:
class A:
    statements...
class B:
    statements...
class C(A,B):
    statements...

#Task2: Bring out a real time scenario for Multiple Inheritance

#Multiple Inheritance --> Whatsapp Scenario --> Send messages, video call

class Messages:
    '''base class 1'''
    def send_message(self):
        print("Used for sending messages")

class Voice_Calls:
    '''base class 2'''
    def voice_call(self):
        print("Used for making voice calls")

class Whatsapp(Messages, Voice_Calls):
    '''derived class'''
    def video_call(self):
        print("Used for making Video Calls")

u1 = Whatsapp()
u1.voice_call()
u1.send_message()
u1.video_call()

#Multilevel Inheritance

#Syntax:

class A:
    statements...
class B(A):
    statements...
class C(B):
    statements...

#Whatsapp --> Users, Business_User, Verified_User --> Multilevel Inheritance

class Users:
    '''Base Class'''
    def send_messages(self):
        print("Used for sending messages")

class Business_User(Users):
    '''Business_user class'''
    def send_bulk_messages(self):
        print("Used for sending bulk messages")

class Verified_User(Business_User):
    '''Verified_user class'''
    def avatars(self):
        print("User can create avatars")

print("Normal User:")
u1 = Users()
u1.send_messages()
print("\n")

print("Business User:")
u2 = Business_User()
u2.send_messages()
u2.send_bulk_messages()
print("\n")

print("Verified User:")
u3 = Verified_User()
u3.send_messages()
u3.send_bulk_messages()
u3.avatars()
print("\n")

#Hybrid Inheritance --> Combination of two or more types of Inheritance

#Example of Hybrid Inheritance --> Electronic Devices --> combination of Multiple and Multilevel Inheritance

class Internet:
    '''Base class 1'''
    def surfing(self):
        print("Used for web Surfing")

class Message:
    '''Base class 2'''
    def message(self):
        print("Used for messaging")

class Camera:
    '''Base class 3'''
    def photos(self):
        print("Used for taking photos")

class Voice_Calls:
    '''Base Class 4'''
    def voice_call(self):
        print("Used for making voice calls")

class Computer(Internet, Message):
    '''Derived class 1'''
    def emails(self):
        print("Used for sending emails")

class Tablet(Computer, Camera):
    '''Derived class 2'''
    def entertainment(self):
        print("Used for entertainment")

class Smart_phone(Tablet, Voice_Calls):
    '''Derived class 3'''
    def calling(self):
        print("Used for emails, internet, entertainment, photos, voice calls and etc...")

comp = Computer()
comp.emails()
comp.message()
comp.surfing()

Tablet = Tablet()
Tablet.entertainment()
Tablet.emails()
Tablet.message()
Tablet.surfing()

Smart_phone = Smart_phone()
Smart_phone.calling()
Smart_phone.entertainment()
Smart_phone.photos()
Smart_phone.message()
Smart_phone.surfing()
Smart_phone.voice_call()

#Polymorphism --> Poly(Many)+Morphism(Forms) --> Many Forms
#Method Overloading, Method Overriding, Operator overloading

#Example: Hotstar --> Free User, VIP User, Premium User

class Hotstar:
    '''Method Overloading scenario'''
    def watch(self):
        print("User has logged in")
    
    def watch(self,movie_name):
        print("Watching Movie:",movie_name)
    
raju = Hotstar()
raju.watch("RRR")

#In the above case same watch() method is overloaded so to make specific usage of, we will make the usage of default arguments

class Hotstar:
    '''Method Overloading scenario'''
    def watch(self,movie_name = None):
        self.movie_name = movie_name
        if self.movie_name == None:
            print("User has logged in")
        else:
            print("Watching Movie:",self.movie_name)
    
raju = Hotstar()
raju.watch()
raju.watch("RRR")

#Method Overloading with variable length arguments (*args)

class Hotstar:
    '''MOL with *args usage'''
    def add_to_list(self,*movies):
        for movie in movies:
            print("Movie added:",movie)
    
user = Hotstar()
user.add_to_list("RRR","Pushpa","KGF")

#Method Overloading with type of arguments usage
class Hotstar:
    '''MOL with type of args usage'''
    def movieslist(self,content):
        if isinstance(content,str):
            print("Playing Content",content)
        elif isinstance(content,list):
            for movie in content:
                print(movie,"added to watchlist")
        else:
            print("Enter valid input")
    
user = Hotstar()
user.movieslist("RRR")
user.movieslist(["RRR","Pushpa","KGF"])

#Method Overriding --> if same method is used in both base and derived class

class FreeUser:
    def watch(self):
        print("Only limited content is available along with ads")

class VIPUser(FreeUser):
    def watch(self):
        super().watch()
        print("All content is available along with ads")

class PremiumUser(VIPUser):
    def watch(self):
        super().watch()
        print("All content is available without ads")

fu = FreeUser()
vu = VIPUser()
pu = PremiumUser()

print("Free User:")
fu.watch()
print("\n")

print("VIP User:")
vu.watch()
print("\n")

print("Premium User:")
pu.watch()
print("\n")

#Polymorphism --> Operator Overloading --> usage of magic methods
#If two operands are numericals, using + operator is addition, if two operands are strings, using + operator is concatenations, if two operands are lists, using + operator is merging

eg:
print(5+6)    #addition    #Output: 11
print('5'+'6')  #concatenations    #Output: '56'
print([5]+[6]) #merging    #Output: [5, 6]

a = 7; b = 8
print(a.__add__(b))   #same as a+b
a = [1,2,3]; b = [4,5,6]
print(a.__add__(b))   #same as [1,2,3]+[4,5,6]
print(a.__len__())  #same as len([1,2,3])
a.__delitem__(1)
print(a)            #same as del a[1]

#Now let us understand how above dunder methods such as __add__, __str__

class WatchHistory:
    '''We want to calculate the watchhistory of user'''
    def __init__(self, hours):
        self.hours = hours
        
a = WatchHistory(120)
b = WatchHistory(40)
print(a.__add__(b))  #AttributeError
print(a.hours.__add__(b.hours))  #160

class WatchHistory:
    '''We want to calculate the watchhistory of user'''
    def __init__(self, hours):
        self.hours = hours
    def __add__(self,value):
        return self.hours + value.hours
    def __str__(self):
        return f"Total Hours {self.hours}"
        
a = WatchHistory(120)
b = WatchHistory(40)
print(a)
print(b)
print(a+b)

#So in above case we are overloading our dunder add method

#Abstraction --> It is one of the key feature of OOP which helps in implementing important information (hiding unneccessary details), if we want to invoke a specific method from a base class to be applied for all derived class
#abc module

from abc import ABC, abstractmethod

#Example of Instagram --> Upload photo, upload video, upload reel, upload story
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass

class Photo_Upload(Content):
    def upload(self):
        print("Photo Uploaded")

class Video_Upload(Content):
    def upload(self):
        print("Video Uploaded")

class Story_Upload(Content):
    def upload(self):
        print("Story Uploaded")

class Reel_Upload(Content):
    def upload(self):
        print("Reel Uploaded")

contents = [Photo_Upload(),Video_Upload(),Story_Upload(),Reel_Upload()]
print("Types of contents:")
for content in contents:
    content.upload()

#The Method name should be same in all the derived classes as the abstractmethod name otherwise, AttributeError occurs

"""
