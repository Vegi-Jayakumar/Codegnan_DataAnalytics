#Print a table of a number
# print("Table Generator")

# number = float(input("Enter a number: "))
# length = int(input("Enter the length: "))

# for i in range(length):
#     print(f"{number} X {i+1} = {number * (i+1)}")


#Print the nearest table number
# digit = int(input("Enter a number: "))
# table_num = int(input("Enter the table number: "))

# k = 0
# ans = 0
# num = 0
# i = 0

# while True:
#     k += table_num
#     i += 1
#     if k > digit:
#         ans = i-1
#         num = k - table_num
#         break

# print(f"The nearest number to {digit} is {num} at a place {ans}")


# num = 5
# if(num == 5):
#     print("The number is 5")

#Check if the string is a palindrome
# string = input("Enter a string: ")
# rev_string = string[::-1]
# if(string == rev_string):
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")


# age = 38
# if(age <= 20):
#     print("he is dependent")
# elif(age >= 65):
#     print("he is dependent")
# else:
#     print("he is independent")


# age = 30
# if(age >= 18):
#     if(age >= 60):
#         print("Senior Citizen")
#     else:
#         print("Adult")
# else:
#     print("Minor")


# attendance = True
# if(attendance):
#     print("He is present")
# else:
#     print("He is absent")


#Perform operations on two numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# operation = input("Enter an operation (+, -, *, /,**, //, %): ")

# match operation:
#     case '+':
#         print(a + b)
#     case '-':
#         print(a - b)
#     case '*':
#         print(a * b)
#     case '/':
#         print(a / b)
#     case '**':
#         print(a ** b)
#     case '//':
#         print(a // b)
#     case '%':
#         print(a % b)
#     case _:
#         print("Invalid operation")


# data_ = {
#     "a" : 0,
#     "Marks" : 0
# }

#even or odd
# data_['a'] = int(input("Enter a number: "))

# if data_['a'] % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#Grading System
# data_["Marks"] = int(input("Enter Marks: "))

# if data_["Marks"] >= 90:
#     print("Grade A+")
# elif data_["Marks"] >= 80:
#     print("Grade A")
# elif data_["Marks"] >= 70:
#     print("Grade B+")
# elif data_["Marks"] >= 60:
#     print("Grade B")
# elif data_["Marks"] >= 50:
#     print("Grade C+")
# elif data_["Marks"] >= 40:
#     print("Grade C")
# elif data_["Marks"] >= 35:
#     print("Grade D")
# else:
#     print("Fail")


#using assert to check the value of a variable
# string_ = "Hello World"
#
# assert string_ == "Hello World", "The string is not Hello World"
# print("The string is Hello World")

#Check if the number is prime
# val_ = int(input("Enter a number: "))

# for i in range(2, val_):
#     if val_ % i == 0:
#         print("The number is not prime")
#         break
# else:
#     print("The number is prime")

'''
write only the approach without the code
1. find out if a number is even or odd

> create a variable an take an integer as an input
> Calculate the remainder/modulus for the number with 2
> if remainder is 0, the number is even
> if remainder is 1, the number is odd

2. remove duplicate from the list

> create a list and take integer inputs and save them in the list.
> create a new empty list.
> create a loop with the length of the list as the range.
> check if the element, present in the list is present in the new list or not.
> if the element is not present in the new list, append it to the new list.
> if the element is present in the list, skip the iteration using continue keyword.
> print the new list. The new list does not contain any duplicate values.

                            or

> create a list and take integer inputs and save them in the list.
> using type conversions convet the list into set and again convert the set into a list.
> The above step removes all the duplicate values.
> print the list.

3. armstrong number check

> create a variable n and take an integer as an input.
> Initilize a variable sum with 0.
> convert the integer variable to find the length and store in a variable.
> Create a temp variable and assign the input to the temp variable.
> create a loop, and find int(n%10) and save it in a variable. This variable gives us the last digit of the number.
> save the power of the length of the new variable to the sum.
> divide 10 from the difference between n and the new variable.
> if n is equal to sum, then the number is armstrong.

                            or

> create a variable n and take an integer as an input.
> Initilize a variable sum with 0.
> convert the integer variable to string to find the length and store in a variable.
> convert the input integer to a string, and save it in a temp variable.
> create a loop with the length of the string as range.
> calculate the int of the power of the element at the i index of the temp variable with the length.
> add the result to the sum variable.
> if the sum variable is equal to n, then the number is armstrong.

4. number of vowels in a string

> create a list containing all the vowels
> take a string as an input.
> create a loop with the length of the string as range, and check if the i element in the string is present in the list of vowels.
> create a sum variable and increment for every occurance of the vowel in the string.
> print the value of the sum variable.

5. count the number of words in a string

> take a string as an input.
> create a loop with the length of the string as range, and check if the i element in the string is a space.
> create a sum variable with the initial value as 1 and increment for every occurance of a space in the string.
> print the value of the sum variable.

'''

#1. find out if a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

#2. remove duplicate from the list
# list = [1, 2, 3, 4, 4, 6, 9, 8, 9, 10]
# new_list = []
# for i in range(len(list)):
#     if list[i] in new_list:
#         continue
#     else:
#         new_list.append(list[i])
# print(new_list)

#                or

# list = [1, 2, 3, 4, 4, 6, 9, 8, 9, 10]
# new_list = list(set(list))
# print(new_list) 

#3. amstrong number check
# var_ = 1634
# len_ = len(str(var_))
# sum = 0
# temp = var_
# for i in range(len_):
#     digit1 = int(temp%10)
#     temp = (temp - digit1) / 10
#     sum += digit1**len_

# if var_ == sum:
#     print("The number is amstrong")
# else:
#     print("The number is not amstrong")

#                or

# var_ = 1634
# len_ = len(str(var_))
# sum = 0
# temp = str(var_)
# for i in range(len_):
#     sum += int(temp[i])**len_

# if var_ == sum:
#     print("The number is amstrong")
# else:
#     print("The number is not amstrong")

#4. number of vowels in a string
# sentence = "Hello World"
# vowels = ['a', 'e', 'i', 'o', 'u']
# sum = 0
# for i in range(len(sentence)):
#     if sentence[i].lower() in vowels:
#         sum += 1
# print(sum)

#5. count the number of words in a string
# sentence = "Hello World"
# sum = 1
# for i in range(len(sentence)):
#     if sentence[i] == " ":
#         sum += 1
# print(sum)
