# Day - 18

'''
math Module:
-> pi = math.pi gives us the pi value of 3.141592
-> ceil = math.ceil(x) rounds up the value of x
-> floor = math.floor(x) rounds down the value of x
-> sqrt = math.sqrt(x) gives the square root of x
-> factorial = math.factorial(x) gives the factorial of x
-> pow = math.pow(x, y) gives x to the power of y
-> sin = math.sin(x) gives the sine of x
-> cos = math.cos(x) gives the cosine of x
-> tan = math.tan(x) gives the tangent of x

random Module:
-> randint(a, b) gives a random number between a and b
-> randrange(start,stop,step) gives a random number between start and stop
-> choice(sequence) gives a random element from the sequence
-> shuffle(sequence) shuffles the sequence
-> sample(population, k) gives k random elements from the population
-> random() gives a random number between 0 and 1

platform Module:
-> platform.system() gives the platform name
-> platform.release() gives the platform release
-> platform.version() gives the platform version
-> platform.machine() gives the platform architecture
-> platform.processor() gives the platform processor
-> platform.platform() gives the platform information

collections module:
-> namedtuple() gives a tuple with named elements
-> Counter() gives a dictionary with counts of elements
-> deque() gives a double-ended queue
-> defaultdict() gives a dictionary with default values
-> Counter(sequence).most_common() gives the most common elements in the sequence

datetime Module:
-> datetime.datetime.now() gives the current date and time
-> datetime.date.today() gives the current date
-> datetime.time(hour, minute, second) gives the time
-> datetime.timedelta(days, hours, minutes, seconds) gives the time difference

strftime () Method:
-> strftime (format) is used to format the date and time

Format Codes:
-> %Y gives the year with 4 digits
-> %y gives the year with 2 digits
-> %m gives the month as a number
-> %b gives the month as a abbreviation
-> %B gives the month as a full name
-> %d gives the day of the month
-> %A gives the day of the week as a full name
-> %a gives the day of the week as a abbreviation
-> %H gives the hour in 24-hour format
-> %I gives the hour in 12-hour format
-> %M gives the minutes
-> %S gives the seconds

itertools Module:
-> count(start,step) gives an iterator that returns evenly spaced values
-> repeat(element,times) gives an iterator that returns the element times
-> cycle(iterable) gives an iterator that returns the elements of the iterable in a cycle
-> chain(iterable1,iterable2) gives an iterator that returns the elements of the iterable1 and iterable2 in a cycle
-> islice(iterable,start,stop,step) gives an iterator that returns the elements of the iterable in a cycle
'''

# import random

# number = random.randint(1, 10)
# chances = 3
# while chances > 0:
#     guess = int(input("Enter your guess: "))
#     if guess == number:
#         print("Your guessed number is correct")
#         break
#     else:
#         print("Your guessed number is wrong")
#         chances -= 1

# if chances == 3:
#     print("You guessed the number in 1 attempt.")
# elif chances == 2:
#     print("You guessed the number in 2 attempts.")
# elif chances == 1:
#     print("You guessed the number in 3 attempts.")
# else:
#     print("You failed to guess the number")
#     print(f"The number is {number}")


