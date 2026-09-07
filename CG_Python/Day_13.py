#Day - 13

'''
Functions
-> A block of code which performs a specific task
-> It is called only when it is needed

Functions are of 2 types
-> built in functions
-> user defined functions

* Built in functions: Built in functions are already defined in the python interpreter.
    Example: print(), input(), type(), id(), len(), range(), etc.

* User defined functions: User defined functions are defined by the user.
    -> A function start with def keyword and the line is called as function definition line, where we can define a function name and parameters.    
    -> Parameters: Parameters are the values that are passed to the function.
    -> Arguments: Arguments are the values that are passed to the function when it is called.

    Syntax: 
        def function_name(parameters):
            function_body
            return value
    Example: 
        def my_function():
            print("Hello World")
        my_function()               # Output = Hello World

        def add_(a,b):
            print(a+b)
        add_(3,7)                   # Output = 10

    Example of return value
        def add_(a,b):
            return a+b
        print(add_(3,7))            # Output = 10

Arguments: Arguments are passed to the function when it is called.

-> Positional Arguments: Positional arguments are the arguments that are passed to the function in the correct order.
    Example: 
        def add_(a,b):
            print(a+b)
        add_(3,7)                   # Output = 10

-> Keyword Arguments: Keyword arguments are the arguments that are passed to the function in the form of key=value pairs. The order of the arguments is not necessary while calling the function.
    Example: 
        def add_(a,b):
            print(a+b)
        add_(b=3,a=7)               # Output = 10

-> Default Arguments: Default arguments are the arguments that are given a default value.
    * The function will only consider the arguments that are given even if the default values are present. If no arguments are given, it will consider the default value.
    Example: 
        def add_(a=3,b=7):
            print(a+b)
        add_()                      # Output = 10

        def add_(a=3,b=7):
            print(a+b)
        add_(6,3)                   # Output = 9

-> Variable Length Arguments: Variable length arguments are the arguments that can take any number of values.
    * The values are passed to the function in the form of tuple.
    * The * operator is used to pass the arguments.
    Example: 
        def add_(*args):
            print(args)
        add_(3,7,4)                 # Output = (3,7,4)

-> Keyword Length Arguments: Keyword length arguments are the arguments that can take any number of values in the form of dictionary.
    * The ** operator is used to pass the key=value arguments.
    Example: 
        def add_(**args):
            print(args)
        add_(a=3,b=7,c=4)           # Output = {'a': 3, 'b': 7, 'c': 4}

Return: The return value is the value that is returned by the function. 
    -> Once the return is executed means it will get back to the place where the function was called. And the function will stop executing from the return statement.
    -> The default return value of the function is None.
    Example: 
        def add_(a,b):
            return a+b
        print(add_(3,7))            # Output = 10
'''
#fibonacci series
# def fibonacci(a):
#     num1 = 0
#     num2 = 1
#     print(f"{a} elements of fibonacci series are:")
#     for i in range(a):
#         print(num1, end=" ")
#         num3 = num1 + num2
#         num1 = num2
#         num2 = num3

# range_ = int(input("Enter the range: "))
# fibonacci(range_)

#prime Numbers
# def isprime(a = 2):
#     count = 0
#     for i in range(2, a):
#         if a % i == 0:
#             count += 1
#     if count == 0:
#         print(f"{a} is prime")
#     else:
#         print(f"{a} is not prime")

# num = int(input("Enter a number: "))
# isprime(num)
