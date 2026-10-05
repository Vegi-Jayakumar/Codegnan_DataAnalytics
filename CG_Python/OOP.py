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

Using SIngle Inheritance we will make use of class attributes and class methods along with the importance of super() (constructor Overriding/Method Overriding)

"""
