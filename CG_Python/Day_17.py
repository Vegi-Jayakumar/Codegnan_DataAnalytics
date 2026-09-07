# Day - 17

'''
Modules:
-> Modules are pre-defined files (.py) containing definitions, variables, functions and classes.

Importing modules:
-> import module_name
-> from module_name import item_name

Example:
-> import math
-> from math import sqrt, pi

-> There are 2 types of modules:
    1. Bulit-in modules (math, random, datetime, os, sys, etc.)
    2. User-defined modules (created by the user)

Built-in modules: These are developed by the programmers and they come with installation of python
-> math module: contains mathematical functions
    example: math.sqrt(16)  # gives the square root of 16
-> random module: contains random number generation functions
    example: random.randint(1, 10)  # gives the random number between 1 and 10
-> datetime module: contains date and time functions
    example: datetime.datetime.now()  # gives the current date and time
-> os module: contains operating system functions
    example: os.getcwd()      # give the location of the current working directory
-> sys module: contains system-specific parameters and functions
    example: sys.version  # gives the version of python

User-defined modules: These are custom files created by the users for convenience.

import specific function from the module
-> from module_name import function_name
-> from module_name import function1, function2, function3
-> from module_name import * (import all functions)

Example:
-> from math import sqrt, pi
-> print(sqrt(16))
-> print(pi)

import modules with alias
-> import module_name as alias_name

Example:
-> import math as mt
-> print(mt.sqrt(16))

'''
