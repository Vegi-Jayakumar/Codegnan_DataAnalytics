#Student Marks Manager

# marks = []
# for i in range(3):
#     mark = int(input("Enter Marks: "))
#     marks.append(mark)

# print(f"marks: {marks}")

# marks.insert(0, 90)
# print(f"marks after inserting 90: {marks}")

# marks.extend([75,85])
# print(f"marks after extending: {marks}")

# marks.remove(75)
# print(f"marks after removing 75: {marks}")

# marks.pop()
# print(f"marks after pop: {marks}")

# print(f"final marks: {marks} and length of the list is {len(marks)}")

#Number List Analyser

# numbers = [20,10,30,20,40,20]

# numbers.sort()
# print(f"Sorted list: {numbers}")

# numbers.reverse()
# print(f"Reversed list: {numbers}")

# num = int(input("Enter a number you want to search: "))
# if num in numbers:
#     print(f"{num} is present in the list")
#     print(f"Count of {num} is {numbers.count(num)}")
#     print(f"Index of {num} is {numbers.index(num)}")
# else:
#     print(f"{num} is not present in the list")

# print(f"Smallest number in numbers is {min(numbers)}")
# print(f"Largest number in numbers is {max(numbers)}")
# print(f"Sum of all numbers is {sum(numbers)}")

#Even and Odd Number Separator
# numbers = [10,15,20,25,30,35]
# even = []
# odd = []

# for num in numbers:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)

# print(f"Even list: {even}")
# print(f"Odd list: {odd}")

# print(f"first 3 digits in numbers: {numbers[0:3]}")
# print(f"Last 3 digits in numbers: {numbers[-3:]}")

# Copy_numbers = numbers.copy()
# numbers.clear()
# print(f"original list: {numbers} and Copied list: {Copy_numbers}")

#Unique Name Manager
# names = ['Asha','Rahul','Asha','John','Rahul']
# unique_names = set(names)
# unique_names.add('Meera')
# unique_names.update(['Arun','Priya'])
# if 'John' in unique_names:
#     unique_names.remove('John')
# if 'David' in unique_names:
#     unique_names.discard('David')

# for name in unique_names:
#     print(f'{name}\n')

#Course Stdent Comparison
# python_students = {'Asha','Rahul','John','Meera'}
# da_students = {'Rahul','Meera','Arun'}

# results = []
# results.append(f"Students in all the courses: {python_students.union(da_students)}")
# results.append(f"Students learning in both Courses: {python_students.intersection(da_students)}")
# results.append(f"Students in Python only: {python_students.difference(da_students)}")
# results.append(f"Students learning only on of the courses: {python_students.symmetric_difference(da_students)}")
# results.append(f"is da_students a subset of python_students? : {da_students.issubset(python_students)}")
# results.append(f"is python_students a superset of da_students? : {python_students.issuperset(da_students)}")
# results.append(f"Are the two sets disjoint?: {python_students.isdisjoint(da_students)}")


# for i  in results:
#     print(i)

