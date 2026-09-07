# Day - 14

'''
Scope of variables
    * Local Variables
    * Global Variables

-> Local Variable: A variable that is defined inside a function and can only be accessed inside the function.
    Example: 
        def my_function():
            a = 10                # local variable
            print(a)              # output = 10
        my_function()             # output = 10
        print(a)                  # output = NameError: name 'a' is not defined

-> Global Variable: A variable that is defined outside a function and can be accessed inside the function and outside the function.
    Example: 
        a = 10                    # global variable
        def my_function():
            print(a)              # output = 10
        my_function()             # output = 10
        print(a)                  # output = 10

global keyword: It is used to refer to a global variable inside a local scope.
    Example: 
        a = 10                    # global variable
        def my_function():
            global a              # output = 10
            a = 20                # output = 20
        my_function()             # output = 20
        print(a)                  # output = 20

passing arguments to the function
* Pass by value
* Pass by reference

-> Pass by reference: When we pass a value using an external variable to the function is called as passing by reference.
    Example: def even_odd(num):
                if num % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
             a = 10                   # global variable
             even_odd(a)              # output = Even

-> Pass by value: When we pass a value directly to the function without using outside variables is called as passing by value.
    Example: def even_odd(num):
                if num % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
             even_odd(10)              # output = Even

Recursive functions: A function that calls itself is called as a recursive function.
    Example: def factorial(num):
                 if num == 0 or num == 1:
                    return 1
                 return num * factorial(num - 1)

            print(factorial(5))


'''
