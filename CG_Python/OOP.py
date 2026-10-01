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

Inheritance: 

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

"""
