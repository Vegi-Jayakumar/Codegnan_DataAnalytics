# Day - 22

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

'''
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
#Fix the program

# file = open('inventory.txt', 'a')
# for i in range(3):
#     try:
#         product = input("Enter product name: ")
#         quantity = int(input("Enter quantity: "))
#         if quantity >= 0:
#             file.write(f"{product},{quantity}\n")
#         else:
#             print("Invalid quantity")
#     except ValueError:
#         print("Invalid quantity")
# file.close()

# try:
#     with open('inventory.txt', 'r') as file:
#         print("\nCurrent Inventory:")
#         for line in file:
#             product, quantity = line.strip().split(',')
#             print(f"{product} - {quantity}")
#         check = input("Enter product to search: ")
#         if check in file:
#             print(f"{check} is available")
#             print(f"Quantity: {quantity}")
#         else:
#             print(f"{check} is not available")
# except FileNotFoundError:
#     print("File not found.")
