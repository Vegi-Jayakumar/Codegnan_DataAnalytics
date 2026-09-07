#Day - 5

'''
Bitwise Operators : Used to perform bitwise operations.
        Eg: &, |, ^, ~, <<, >>
        & : Bitwise AND : Performs a bitwise AND operation on two numbers.
            Eg: a = 10
                b = 20
                10 --> 01010
                20 --> 10100
                print(a & b)  # Output: 0
        | : Bitwise OR : Performs a bitwise OR operation on two numbers.
            Eg: a = 10
                b = 20
                print(a | b)  # Output: 30
        ^ : Bitwise XOR : Performs a bitwise XOR operation on two numbers.
            Eg: a = 10
                b = 20
                print(a ^ b)  # Output: 30
        ~ : Bitwise NOT : Performs a bitwise NOT operation on a number.
            Eg: a = 10
                print(~a)  # Output: -11
        << : Bitwise Left Shift : Performs a bitwise left shift operation on a number.
            Eg: a = 10
                print(a << 2)  # Output: 40
        >> : Bitwise Right Shift : Performs a bitwise right shift operation on a number.
            Eg: a = 10
                print(a >> 2)  # Output: 2

input formating 
-> integer: int(input())
    Eg: number = int(input("Enter a number: "))
-> float: float(input())
    Eg: number = float(input("Enter a decimal number: "))
-> string: input()
    Eg: name = input("Enter a name: ")
-> list: list(map(int, input().split()))
    Eg: numbers = list(map(int, input("Enter a list of numbers: ").split()))
-> tuple: tuple(map(int, input().split()))
    Eg: numbers = tuple(map(int, input("Enter a tuple of numbers: ").split()))
-> set: set(map(int, input().split()))
    Eg: numbers = set(map(int, input("Enter a set of numbers: ").split()))

Evaluate
-> eval() : Evaluates the given expression.
    Eg: data = eval(input("Enter data: "))
        print(data)
        print(type(data))

Output Formating
-> Standard formating: different datatypes are saperated by commas.
    Eg: name = "Jayakumar"
        age = 22
        print("My name is ", name, "and I am ", age, "years old.")  # output: My name is Jayakumar and I am 22 years old.

-> f-String Formating: Formates a string by embedding expressions inside curly braces. begins with 'f' or 'F' before the opening quote.
    Eg: name = "Jayakumar"
        age = 22
        print(f"My name is {name} and I am {age} years old.")  # output: My name is Jayakumar and I am 22 years old.

-> Modular String Formating: Formates a string by using the % operator. The % operator is used to substitute the values into the string.
    Eg: name = "Jayakumar"
        age = 22
        print("My name is %s and I am %d years old." % (name, age))  # output: My name is Jayakumar and I am 22 years old.

'''

