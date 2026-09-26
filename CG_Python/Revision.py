# Revision

'''
Tokens: Keywords,variables,operators,punctuations,Literals

variables should not start with number, spaces, & any other symbols other than underscore.

batch = ['name','python']
print(batch)        # Output: ['name','python']
print(type(batch))  #everything is an object (POP --> OOP)      # Output: <class 'list'>

len() --> returns the numbr of items in a collection

print(len(batch))   # Output: 2

Add 3 more student names into it
List --> Collection --> append(),extend(),insert()

batch.append('Java')
print(batch)         # Output: ['name','python','Java']
batch.append(['C++','C','Data Science'])
print(batch)         # Output: ['name','python','Java',['C++','C','Data Science']]
batch.extend(['C++','C','Data Science'])
print(batch)         # Output: ['name','python','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
batch.insert(2,'Swift') #inserts given value at specific index for positive index and before the specified index for negative index.
print(batch)         # Output: ['name','python','Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
print(len(batch))    # Output: 7

Indexing --> positive index --> from left to right --> starts with 0 and ends with len(obj)-1
             negative index --> from right to left --> starts with -1 and ends with -len(obj)

batch[0] --> 'name'
batch[1] --> 'python'
batch[-1] --> 'C'
batch[-2] --> 'C++'
batch[35] --> IndexError

Slicing --> [start:stop]       #Start is included and end is excluded; Step is optional
batch[0:3]          #Output: ['name','python','Swift']
batch[4:6]          #Output: ['C++','C']
batch[-3:]          #Output: ['C++','C','Data Science']

Striding --> [start:stop:step]
batch[::2]          #Output: ['name','Swift',['C++','C','Data Science'], 'C++']
batch[::3]          #Output: ['name','Java','c']
batch[1:5:2]        #Output: ['python','Java']

#Tryout in notes with explanation
print(batch[:7:4])       #Output: ['name',['C++','C','Data Science']]
print(batch[7::4])       #Output: ['Data Science']
print(batch[1::5])       #Output: ['python','C']
print(batch[1:7:-2])     #Output: []
print(batch[-1:-4:-1])   #Output: ['Data Science', 'C', 'C++']

batch = ['name','python','Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
batch.insert(2,('HTML','CSS','Javascript'))
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']

sub-indexing
print(batch[2][0:2])    #Output: ('HTML', 'CSS')
print(batch[2][1])      #Output: 'CSS'
print(batch[2][::2])    #Output: ('HTML', 'Javascript')

index position
print(batch[2].index('HTML'))           #Output: 0
print(batch[2].index('CSS'))            #Output: 1
print(batch[2].index('Javascript'))     #Output: 2
print(batch[2].index('java'))           #Output: ValueError
print(batch[2].count('java'))           #Output: 0

#Convert string into uppercase
batch[5][2] = batch[5][2].upper()
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE'], 'C++','C','Data Science']

#Insert element in sub-list
batch[5].append('Python')
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C++','C','Data Science']

#Removing Elements -->remove(value),pop(index),clear()

batch.remove('C++')
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C','Data Science']
batch[2].pop()
print(batch)        #Output: AttributeError
del batch[2][1]     #Output: TypeError

#concatinating a tuple
batch[2] = batch[2]+('Jsp',)
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript','Jsp'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C','Data Science']

#Dictionaries --> {k:v}, keys must be unique, they can be int, str, float, list
P_lang = {}
P_lang['Frontend'] = ['html','css','js']
P_lang['Backend'] = ['py','nodejs','expressjs']
P_lang['Database'] = ['mysql','mongodb','postgresql']
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql']}

#update dictionary --> dict_1.update(dict_2)
P_lang.update({'Frameworks':['react','angular','vue'],
               'Tools':('github','IDE')})
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql'], 'Frameworks': ['react', 'angular', 'vue'], 'Tools': ('github', 'IDE')}

#keys in dictionary
print(P_lang.keys())       #Output: dict_keys(['Frontend', 'Backend', 'Database', 'Frameworks', 'Tools'])

#add values to keys is a dictionary
P_lang['Frameworks'].append('React Native')
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql'], 'Frameworks': ['react', 'angular', 'vue', 'React Native'], 'Tools': ('github', 'IDE')}

#Tasks to be done
create a dictionary using codegnan portal as example. keys:Exams,Mock Interviews, Project Demos.
push to github --> share your link in whatsapp group.

#input formatting
a,b = 13,4.5

#Output formatting
print(a,b)  #Default sep = ' '
print(a,b,sep=',')
print(a,b,sep=':')
print('codegnan','python','vizag',sep='--->')

#end by default throws new line, we can modify it...
print(a,b,end=' ')
print("Codegnan is in vizag",end="\t")
print("DA6 and PFS6")

number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
operator = input("Enter an operator (+,-,*,/): ")

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)
else:
    print("Invalid operator")

#          or 

number_1, number_2 = map(int, input("Enter values: ").split()); operator = input("Enter an operator (+,-,*,/): ")
result = number_1+number_2 if operator == "+" else number_1-number_2 if operator == "-" else number_1*number_2 if operator == "*" else number_1/number_2 if operator == "/" else "Invalid operator"
print("Result:",result)

#usage of %d,%f,%s  --> prefer this only when you are working on calculations
price = 45.99; grade = 'A'; stock = 15
print("the price of %d books of %s grade is %.2f" %(stock,grade,price))

radius = 3.5; area = 3.1416*(radius**2)
print("the area of a circle with radius %.1f is %.2f" %(radius,area))

#f-string --> most recommended
name = "Codegnan"; domain = "Python"; location = "Vizag"
print(f"The {domain} program is currently running in {name} at {location}")

#Control Block Statements  --> They control the flow of the program based on certain conditions. They are of three types, they are: conditional statements, loop statements and Jumping statements.
#Conditional statements --> if, elif, else
#Loop statements --> for, while
#Jumping statements --> break, continue, pass

#BMI

data_ = {
    'height' : [],
    'weight' : [],
    'bmi' : []
}

rounds = int(input("Enter number of rounds: "))
for i in range(rounds):
    #Height Input
    height_format = int(input("Enter height format: 1.ms 2.cms 3.fts \nchoice:"))
    if height_format == 1:
        input_ = float(input("Enter height in ms: "))
        height = input_
    elif height_format == 2:
        input_ = int(input("Enter height in cms: "))
        height = input_ /100
    elif height_format == 3:
        input_ = float(input("Enter height in fts: "))
        height = input_ / 3.281
    else:
        print("Invalid input")
    data_['height'].append(height)

    #Weight Input
    weight_format = int(input("Enter weight format: 1.kgs 2.lbs \nchoice: "))
    if weight_format == 1:
        input_ = int(input("Enter weight in kgs: "))
        weight = input_
    elif weight_format == 2:
        input_ = float(input("Enter weight in lbs: "))
        weight = input_ / 2.205
    else:
        print("Invalid input")
    data_['weight'].append(weight)

    #Conditions
    if (0 <= data_['height'][i] <= 2.5) and (0 <= data_['weight'][i] <= 200):
        data_['bmi'].append(data_['weight'][i]/(data_['height'][i]**2))
        print("BMI = %.1f"%data_['bmi'][i])
        if data_['bmi'][i] < 18.5:
            print("UnderWeight")
        elif data_['bmi'][i] < 24.9:
            print("Healthy weight")
        elif data_['bmi'][i] < 29.9:
            print("Overweight")
        else:
            print("Obesity")
    else:
        print("Invalid input")

#Exception Handling --> It is a mechanism to a program which responds to run time errors or compilations.
#Exception --> It tries to make our program go in a normal flow.
keywords --> try, except, else, finally, raise, assert

try:
    a, b = map(int, input("Enter two values: ").split())
    result = a/b
    print("Result = ",result)
# except Exception as e:
#    print(e)
# except ValueError:
#     print("Enter only Numbers")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
except (ValueError,ZeroDivisionError) as e:
    if type(e) == ValueError:
        print("Enter only Numbers")
    elif type(e) == ZeroDivisionError:
        print("Cannot divide by zero")
    elif type(e) == NameError:
        print("Check your program")
finally:
    print("Program ended")


# In above case we will get ValueError, ZeroDivisionError...
possible types of errors --> TypeError, ValueError, IndexError, ZeroDivisionError, NameError, AttributeError, ArithmeticError...

# #Marks Classification

# try:
#     marks = int(input("Enter Marks: "))

#     if 0 <= marks <= 100:
#         if marks >= 90:
#             print("Grade: A")
#             print("Remark: Outstanding!")
#         elif marks >= 80:
#             print("Grade: B")
#             print("Remark: Excellent!")
#         elif marks >= 70:
#             print("Grade: C")
#             print("Remark: Good!")
#         elif marks >= 60:
#             print("Grade: D")
#             print("Remark: Fair, needs improvement")
#         elif marks >= 50:
#             print("Grade: E")
#             print("Remark: Poor, needs serious improvement")
#         else:
#             print("Grade: F")
#             print("Remark: Failed, needs to reappear")

#     else:
#         print("Invalid marks entered")
# except ValueError:
#     print("Invalid marks entered")


#Even odd checker with twist
# try:
#     number = int(input("Enter a number:"))

#     if number == 0:
#         print("Zero is neither even or odd")
#     elif number % 2 == 0:
#         if number > 0:
#             print("Even number")
#         else:
#             print("Negative Even number")   
#     else:
#         if number > 0:
#             print("Odd number")
#         else:
#             print("Negative Odd number")
# except ValueError:
#     print("Please Enter a number only")


#Season Identifier
# try:
#     month_number = int(input("Enter month number: "))

#     if 1 <= month_number <= 12:
#         if month_number == 12 or month_number == 1 or month_number == 2:
#             print("Season: Winter")
#         elif month_number == 3 or month_number == 4 or month_number == 5:
#             print("Season: Spring")
#         elif month_number == 6 or month_number == 7 or month_number == 8:
#             print("Season: Summer")
#         else:
#             print("Season: Autumn")
#     else:
#         print("Invalid month entered")
# except ValueError:
#     print("Invalid month entered")

#Updated BMI Calculator

data_ = {
    'height' : [],
    'weight' : [],
    'bmi' : []
}

count = 0
try:
    while count<10:
        #Height Input
        height = 0
        height_format = int(input("Enter height format: 1.ms 2.cms 3.fts \nchoice:"))
        if height_format == 1:
            input_ = float(input("Enter height in ms: "))
            height = input_
        elif height_format == 2:
            input_ = int(input("Enter height in cms: "))
            height = input_ /100
        elif height_format == 3:
            input_ = float(input("Enter height in fts: "))
            height = input_ / 3.281
        else:
            print("Invalid input")
        data_['height'].append(height)

        #Weight Input
        weight = 0
        weight_format = int(input("Enter weight format: 1.kgs 2.lbs \nchoice: "))
        if weight_format == 1:
            input_ = int(input("Enter weight in kgs: "))
            weight = input_
        elif weight_format == 2:
            input_ = float(input("Enter weight in lbs: "))
            weight = input_ / 2.205
        else:
            print("Invalid input")
        data_['weight'].append(weight)

        #Conditions
        if (0 <= data_['height'][count] <= 2.5) and (0 <= data_['weight'][count] <= 200):
            data_['bmi'].append(data_['weight'][count]/(data_['height'][count]**2))
            print("BMI = %.1f"%data_['bmi'][count])
            if data_['bmi'][count] < 18.5:
                print("UnderWeight")
            elif data_['bmi'][count] < 24.9:
                print("Healthy weight")
            elif data_['bmi'][count] < 29.9:
                print("Overweight")
            else:
                print("Obesity")
        else:
            print("Invalid input")
        count += 1
    print(data_)
except Exception as e:
    print(e)

File Handling --> create files, make some changes over files,
we will use open(), close() file operations.
we will use modes like 'r', 'w', 'a', 'r+' default mode is 'r'
we will use methods like readline(), read(), readlines(), writeline(), write(), writelines()
we can use with keyword to make the file handling more easier. When we are using with keyword we don't have to close the file manually.

# file = open('sample.txt','r')
#print(file.read())
#print(file.readline())
#print(file.readlines())
# file.close()

# file = open('test.txt','w')
# file.write("This is a sample text file created using 'w' mode from file handling.")
# print(file)
# file.close()

# file = open('test.txt','a')
# file.write("\nThis is an appended text file created using 'a' mode from file handling.")
# print(file)
# file.close()

file = open('sample.txt', 'r+')
print(file)
print(file.read())
file.write('appended ')
file.close()

# with open('test.txt','r') as file:
#     print(file.read())


#Student Marks File Manager

# file = open('marks.txt','w')
# for i in range(5):
#     try:
#         marks = int(input("Enter student mark: "))
#         if 0<=marks<=100:
#             file.write(f"{marks}\n")
#             print("Mark saved successfully")
#         else:
#             print("Invalid mark")
#     except ValueError:
#         print("Invalid mark")
# file.close()

# with open('marks.txt','r') as file:
#     print("Saved Marks: ")
#     for line in file:
#         print(line.strip())


#Expense Tracker

# file = open('expenses.txt','w')
# for i in range(5):
#     try:
#         amount = float(input(f"Enter expense {i+1}: "))
#         if amount > 0:
#             file.write("%.1f\n"%amount)
#         else:
#             print("Invalid expense. Please enter a number.")
#     except ValueError:
#         print("Invalid expense. Please enter a number.")
# file.close()

# try:
#     with open('expenses.txt','r') as file:
#         print("\nExpenses:")
#         total = 0
#         for line in file:
#             print(line.strip())
#             total += float(line.strip())
#         print("\nTotal expense: %.1f"%total)
# except FileNotFoundError:
#     print("File not found.")


#Student Attendance Manager

# file = open('attendance.txt','w')
# for i in range(5):
#     try:
#         name = input(f"Enter student name: ")
#         a_status = input("Enter attendance (P/A): ")
#         if a_status.upper() in 'PA':
#             file.write(f"{name},{a_status}\n")
#         else:
#             print("Invalid attendance status.")
#     except ValueError:
#         print("Invalid input.")
# file.close()

# try:
#     with open('attendance.txt','r') as file:
#         print("\nPresent Students:")
#         for line in file:
#             name, status = line.strip().split(',')
#             if status.upper() == 'P':
#                 print(name)
# except FileNotFoundError:
#     print("File not found.")


#Product Inventory manager

# file = open('inventory.txt', 'a')
# for i in range(3):
#     try:
#         product_name = input('Enter product name: ')
#         quantity = int(input('Enter quantity: '))
#         if quantity >= 0:
#             file.write(f'{product_name},{quantity}\n')
#         else:
#             print('Quantity cannot be negative')
#     except ValueError:
#         print('Invalid quantity is entered.')
# file.close()

# try:
#     with open('inventory.txt', 'r') as f:
#         print('\nCurrent Inventory:')
#         records = f.readlines()
#         for record in records:
#             product_name, quantity = record.strip().split(',')
#             print(f'{product_name} - {quantity}')
#         search_name = input('\nEnter product to search: ').strip()
#         found = False
#         for record in records:
#             product_name, quantity = record.strip().split(',')
#             if product_name.lower() == search_name.lower():
#                 print(f'{product_name} is available.\nQuantity: {quantity}')
#                 found = True
#         if found == False:
#             print('Product not found')
# except FileNotFoundError:
#     print('Inventory file not found')


#Student Result File Analyzer

# passed=0
# failed=0
# total=0
# valid_students=0
# try:
#     with open('students.txt','r')as f:
#         for record in f:
#             try:
#                 name,mark=record.strip().split(',')
#                 mark=int(mark)
#                 if mark>=50:
#                     result='Pass'
#                     passed+=1
#                 else:
#                     result='Fail'
#                     failed+=1
#                 print(f'{name} - {mark} - {result}')
#                 total+=mark
#                 valid_students+=1
#             except ValueError:
#                 print(f'Invalid mark for {name}\n')
#         avg=total/valid_students     
#         print('-'*25)
#         print('Result Summary')
#         print('-'*25)
#         print(f'Passed students: {passed}')
#         print(f'Failed students: {failed}')
#         print('Average mark: %.2f'%avg)
# except FileNotFoundError:
#     print('students.txt file not found')

Nested Loops --> (for in for) --> These are primarily used for pattern printings matrix operations and problems solving scenarios (data structures)..
inner loop will be completely executed for every outer loop

for i in range(2):  #i=0,1
    for j in range(2):  #j=0,1
        print(f"i={i}, j={j}")

In above case for complete j value of 0, i value will be 0,1,2 and follows same for others
outer loop defines rows, inner loop defines columns

for i in range(2):
    for j in range(i):
        print(f"i={i},j={j}")   #output: i=1,j=0

for i in range(2):
    for j in range(i+1):
        print(f"i={i},j={j}")

for i in range(2):
    for j in range(i-1):    #as here for i=0,j becomes -ve, i=1 j becomes 0
        print(f"i={i},j={j}")   #Output = i=2,j=0

for i in range(3):
    for j in range(3):
        print("*")

for i in range(4):
    for j in range(4):
        print(chr(65+j),end=" ")
    print()


# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# num = 1
# for i in range(4):
#     for j in range(i+1):
#         print(num,end=" ")
#         num+=1
#     print()


# for i in range(5):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()


# inverted triangle
# for i in range(5):
#     for j in range(i, 5):
#         print('*',end=" ")
#     print()


# pyramid pattern
# for i in range(5):
#     for j in range(5-i):
#         print("",end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()


# inverted pyramid pattern
# for i in range(5):
#     for j in range(i+1):
#         print("",end=" ")
#     for k in range(5-i):
#         print("*", end=" ")
#     print()


# floyd's triangle
# char = 65
# for i in range(4):
#     for j in range(i+1):
#         print(chr(char), end=" ")
#         char+=1
#     print()


# number triangle
# for i in range(5):
#     for j in range(i+1):
#         print(i,end=" ")
#     print()


# Character triangle
# char = 65
# for i in range(4):
#     for j in range(i+1):
#         print(chr(char), end=" ")
#     char+=1
#     print()


# diamond pattern
# for i in range(5):
#     for j in range(5-i):
#         print("",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(4):
#     for j in range(i+2):
#         print("",end=" ")
#     for k in range(4-i):
#         print("*",end=" ")
#     print()

functions --> a function is a block of code that performs a specific task
types of functions: user-defined functions, builtin functions, anonymous functions(lambda), recursive functions

> User-defined functions

def function_name(parameters):
    """Doc string (describe your function)"""
    function statements
    return values

function_name(arguments)

types of arguments: positional arguments, keyword arguments, default arguments, variable length arguments, keyword variable length arguments

positional arguments --> order of arguments in function definition and function call should match
keyword arguments --> name of the arguments should match, order doesn't matter
default arguments --> we can make any number of arguments as default. but we have a thumb rule: only first argument cannot be default, non-default arguments can be assigned after default arguments.
variable length arguments --> (*args) --> we can pass any number of arguments, but the data will be stored in a tuple, but we use *args as representation. we can change 'args' but we must include '*' before the parameter.
keyword variable length arguments --> (**kwargs) --> we can pass any number of arguments in the form of key-value pairs, but the data will be stored in a dictionary, but we use **kwargs as representation. we can change 'kwargs' but we must include '**' before the parameter.

def new(*a):
    """usage of variable length arguments"""
    print(a)
    print(type(a))

new(1,2,3,4,5,6,7,8,9,10)
new()   # it returns empty tuple as we did not pass any arguments
new(["hello","World",69])   # it returns list inside a tuple and considers the list as 1 element
new(*["Hello","World",69])  # it unpacks the list and returns individual elements in a tuple  
a,*b,c = 1,"Hello","World",69   # 1 is assigned to a, 69 is assigned to c, and the values in between are assigned to b in the form of list
* can also be used to unpack the values from a collection: print(*[1,"Hello","World",69])  # output: 1 Hello World 69

# Task:
def sum(*args):
    """Sum of all the arguments passed to the function"""
    total = 0
    for i in args:
        #we can use isinstance(i,(int,float)) in if-else statement.
        # if isinstance(i,(int,float)):
        #   total+=i
        # else:
        #   continue 
        #we can use type(i) to verify the type of input
        # if type(i) == int or type(i) == float:
        #   total+=i
        #we can use try-except block to handle the error and continue, but it's not recommended to use try-except for control flow.
        try:
            total+=i
        except TypeError:
            continue
    return total

print(sum(1,2,3,'Hi','Hello',4,5,6,7,8,9))

def admission(**kwargs):
    """usage of keyword variable length arguments"""
    print(kwargs)
    print(type(kwargs))

admission()  #it returns empty dictionary as we did not pass any arguments
admission(name="John", age=20, course="Computer Science")
admission(**{"name": "John", "age": 20, "course": "Computer Science"})  #it unpacks the dictionary and returns individual key:value pairs in a dictionary

# Task: 
def simple(*args,**kwargs):
    """Usage of *args and **kwargs"""
    total = 0
    for i in args:
        total+=i
    print(total)
    for key,value in kwargs.items():
        print(f"key is {key} and value is {value}")

simple(1,2,3,4,5,6,7,8,9,10,name="John", age=20, course="Computer Science")

Scope of the variables --> Scope is basically the region or area where the data is accessible.
> Local scope --> variable(s) defined inside the function are accessible only inside that function.
> global scope --> variable(s) defined outside the function are accessible from anywhere in the program.
> global keyword --> we have to use this keyword to perform operations on a global variable inside a function.
> enclosing scope(nonlocal keyword) --> we use non local keyword to perform operations on a variable(s) defined inside a enclosing function. It is mainly used for nested functions.
> built-in scope --> Usage of built-in functions as variables is strictly not recommended as it may lead to confusion.
> LEGB rule --> Local, Enclosed, Global, Built-in (the order of searching the variables in the scope)

> Built-in functions

#print(dir()) #list all the available built in functions
#print(dir(__builtins__)) # it returns list of all the built-in functions and errors
every builtin datatype is builtin function --> int, float, str, list, tuple, set, dict, bool
print(float(int(bool(24)))) #output: 1.0 # functions as first class objects

# None, '', 0, False, [], {}, () are considered as False or empty values.

#all() and any()
> all() --> returns true if all the elements in the iterable are true or if the iterable is empty, else it returns false
> any() --> returns true if any of the elements in the iterable are true, else it returns false

print(bin(12))                  #binary # output: 0b1100
print(chr(67))                  #character # output: C
print(ord('A'))                 #ordinal # output: 65
print(divmod(6,2))              #division and modulo # output: (3, 0)
print(pow(4,3))                 #power # output: 64
print(round(5.349761,2))        #round # output: 5.35

#filter(), map(), zip(), enumerate()

> Anonymous Functions (lambda)
these are nameless functions (helper functions), we define them by using lambda keyword
syntax: lambda arguments:expression

areaOfRectangle = lambda l,b : l * b
print(areaOfRectangle(7, 4))        #Output: 28

areaOfSquare = lambda s : s**2 
print(areaOfSquare(5))              #Output: 25

#Task : firstname, lastname = fullname --> using lambda functions 

fname = input("Enter first name: ").strip()
lname = input("Enter last name: ").strip()

fullname = lambda fn, ln : fn.title() + " " + ln.title()
print(fullname(fname, lname))

#Task : Even or Odd --> using lambda functions

num = int(input("Enter a Number: "))
iseven = lambda num: "Even" if num % 2 == 0 else "Odd"
result = lambda num: num ** 2 if num % 2 == 0 else num ** 3
print(iseven(num))
print(result(num))

names = ["John", "Peter", "Rohan", "Jane"]
g = lambda x: x in names
h = lambda names, x: names[x]
print(g("John"))  #Output: True
print(h(names,2))   #Output: Rohan

#filter() --> we want to have specific filtered result

data = [1,2,3,4,5,6,7,8,9,10]

new_data = list(filter(lambda x: x%2 == 0,data))
print(new_data) # output: [2, 4, 6, 8, 10]

#Task: filter desired names from the list

names = ['Saketh','Python','Akash','Neha','Sameer']
new_names = filter(lambda i : len(i) >= 6,names)
print(list(new_names)) # output: ['Saketh', 'Python', 'Sameer']

#map() --> it maps the elements of the iterable to the function and returns the result

data = [1,2,3,4,5]

new_data = list(map(lambda x: x*2,data))
print(new_data) # output: [2, 4, 6, 8, 10]

#Task : multiply two lists --> using map function

lst1 = list(map(int,input("Enter first list: ").split()))
lst2 = list(map(int,input("Enter second list: ").split()))

new_data = list(map(lambda x,y: x*y,lst1,lst2))
print(new_data)

#reduce --> functools module
#reduce --> it will check the condition and make it to a single value

from functools import reduce

data = [1,2,3,4,5]

new_data = reduce(lambda x,y: x*y,data)
print(new_data) # output: 120

#Task:find the sum and product of all elements in a list using functions

data = [1,2,3,4,5]

def sum(data):
    sum = 0
    for i in data:
        sum +=i
    return sum

def product(data):
    product = 1
    for i in data:
        product *=i
    return product

print(sum(data))    #output: 15
print(product(data)) #output: 120

#Recursive Fundtions: A function can call itself.
#factorial, fibonacci, sum of numbers......
#recursive functions --> Basecase (it tells when to stop the recursion)
                     --> Resursive case (it tells how to start recursion)

#factorial using recursion

n = int(input("Enter value for factorial: "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n<0:
        return "Input must be a non-negative integer"
    else:
        return n * factorial(n-1)

print(factorial(n))

Functions are first class objects
functions can pass another function as argument
function can return another function
function can be inside another function
function can call itself

modules --> a python file containing variables, functions, and classes, objects.
user-defined modules (import), built-in modules, available modules (pypi)

# import sampleModule as sm
# # print(dir(sm))
# # print(type(sm.data))
# # print(type(sm.details))

# print(sm.data)
# sm.details('Jayakumar','Visakhapatnam') # Here we are accessing via module name

#from keyword helps you to get required attributes from the module without importing the whole module

# import sampleModule
# from sampleModule import data
# print(data.items())
#print(details()) raises error as its not imported
# print(sampleModule.__doc__) #it returns the docstring (description) of the module.

#We can use * to get all the attributes and methods of a module. But it's not recommended as it wastes memory and can lead to name collision.
# from sampleModule import *
# print(data.items())

'''