#Convert to celsius to farhenheit
# celsius = int(input("Enter the temperature in celsius: "))

# fahrenheit = (celsius * 1.8) + 32
# print(f"The temperature in fahrenheit is {fahrenheit}")

##1. calculate the area of a rectangle
# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))
# area = length * breadth
# print(f"The area of the rectangle is {area}")

##2. Print greetings
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello, {name}! You are {age} years old.")

##3. check if even or odd
# a = int(input("Enter a number: "))
# check = lambda a : "Number is Even" if a % 2 == 0 else "Number is Odd"
# print(check(a))

##4. Find max and min in the list
# def max_min(list_num):
#     max_ = list_num[0]
#     min_ = list_num[0]
#     for i in list_num:
#         if i > max_:
#             max_ = i
#         if i < min_:
#             min_ = i
#     return max_, min_

# numbers = list(map(int, input("Enter numbers: ").split()))
# max_, min_ = max_min(numbers)
# print(f"The maximum number is {max_}")
# print(f"The minimum number is {min_}")

##5. check if a string is a palindrome
# string_ = input("Enter the string: ")
# rev_string_ = ""
# for i in string_:
#     rev_string_ = i + rev_string_
# if rev_string_ == string_:
#     print(f"The string is a palindrome")
# else:
#     print(f"The string is not a palindrome")

##6. calculate compound interest
# principle_amount = int(input("Enter the principle amount: "))
# rate_of_interest = int(input("Enter the rate of interest: "))
# number_of_years = int(input("Enter the number of years: "))
# total_amount = principle_amount * (1 + rate_of_interest / 100) ** number_of_years
# compound_interest = total_amount - principle_amount
# print(f"The compound interest is {compound_interest}")

##7. convert days into years months weeks and days
# days = int(input("Enter the number of days: "))
# years = days // 365
# months = (days % 365) // 30
# weeks = ((days % 365) % 30) // 7
# days_ = ((days % 365) % 30) % 7
# print(f"{days} is equal to {years} years {months} months {weeks} weeks {days_} days")

##8. sum of all positive numbers
# def sum_positive_numbers(num_list):
#     sum_ = 0
#     for num in num_list:
#         if num > 0:
#             sum_ += num
#     return sum_

# numbers = list(map(int, input("Enter the numbers: ").split()))
# print(sum_positive_numbers(numbers))

##9. Count number of words in a string
# def count_words(string_):
#     return len(string_.split())

# string_ = input("Enter the string: ")
# print(count_words(string_))

##10. Program to swap two numbers without using a third variable
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# a, b = b, a
# print(f"The first number is {a}")
# print(f"The second number is {b}")

##11. find sum and average of n numbers
# def sum_and_average(num_list):
#     sum_ = 0
#     for num in num_list:
#         sum_ += num
#     return sum_, sum_ / len(num_list)

# numbers = list(map(int, input("Enter the numbers: ").split()))
# sum_, average_ = sum_and_average(numbers)
# print(f"The sum of the numbers is {sum_}")
# print(f"The average of the numbers is {average_}")

##12. temperature from celsius to kelvin
# celsius = int(input("Enter the temperature in celsius: "))
# kelvin = celsius + 273.15
# print(f"The temperature in kelvin is {kelvin}")

##13. check if the string is a palindrome
# string = input("Enter the string: ")
# rev_string = ""
# for i in string:
#     rev_string = i + rev_string
# if rev_string == string:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")

##14. create a function to reverse a given string
# def rev_string(string):
#     rev = ""
#     for i in string:
#         rev = i + rev
#     return rev

# string = input("Enter the string: ")
# print(rev_string(string))

##15. concatinate the list of names with spaces
# names = list(map(str, input("Enter the names: ").split()))
# all_names = ""
# for name in names:
#     all_names = all_names + " " + name

# print(all_names)

##16. check if a string is a pangram
# string_ = input("Enter a string: ").lower()
# alphabets = "qwertyuiopasdfghjklzxcvbnm"
# ispangram = True
# for letter in alphabets:
#     if letter not in string_:
#         ispangram = False
#         break

# if ispangram == True:
#     print("The string is a pangram")
# else:
#     print("The string is not a pangram")

##17. calculate area and circumference of a circle
# radius = int(input("Enter the redius of the circle: "))
# area = 3.14 * (radius ** 2)
# circumference = 2 * 3.14 * radius
# print(f"The area of the circle is {area}")
# print(f"The circumference of the circle is {circumference}")

##18. minutes to hours and minutes
# minutes = int(input("Enter the minutes: "))
# hours = minutes // 60
# minutes_ = minutes % 60
# print(f"The minutes are {hours} hours and {minutes_} minutes")

##19. create a function to count the number of vowels in a string
# def count_vowels(string_):
#     count = 0
#     for i in string_:
#         if i in "aeiou":
#             count += 1
#     return count

# data_ = input("Enter the string: ").lower()
# count = count_vowels(data_)
# print(f"The number of vowels in the string is {count}")

##20. check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     factors = 0
#     for i in range(2, number):
#         if number % i == 0:
#             factors += 1
#     if factors == 0:
#         return True
#     else:
#         return False

# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")

##21. Check if a year is a leap year or not
# def check_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# year = int(input("Enter a year: "))
# if check_leap(year):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

##22. 