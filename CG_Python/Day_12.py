#Day - 12

'''
Loops: Loops are used to execute a block of code repeatedly.
    -> There are 2 types of loops in Python:
        1. For Loop
        2. While Loop

-> For Loop: It is used to iterate over a sequence of values (String, List, Tuple, Set, Dictionary).
    -> Syntax: for <iterator variable/instance variable> in <sequence>:
                    <statement>
    -> Example: for i in range(5):
                    print(i)
        -> Output: 
            0
            1
            2
            3
            4

    -> Else in for loop: The else block is executed when the loop completes normally (without any break).
    -> Example: for i in range(5):
                    print(i)
                else:
                    print("Loop completed")
        -> Output: 
            0
            1
            2
            3
            4
            Loop completed
    -> Example: for i in range(10):
                    if i % 2 ==0:
                        print(f"{i} is an even number")
                    else:
                        print(f"{i} is an odd number")
        -> Output:
            0 is an even number
            1 is an odd number
            2 is an even number
            3 is an odd number
            4 is an even number
            5 is an odd number
            6 is an even number
            7 is an odd number
            8 is an even number
            9 is an odd number

-> While loop: It is used to execute a block of code repeatedly while a condition is true.
    -> Syntax: while <condition>:
                    <statement>
    -> Example: i = 0
                while i < 5:
                    print(i)
                    i += 1

Control Statements: Control statements are used to control the flow of execution of the program.
    -> There are 3 types of control statements in Python:
        1. Break
        2. Continue
        3. Pass

-> break: The break statement is used to exit the loop.
    -> Syntax: break
    -> Example: for i in range(5):
                    if i == 3:
                        break
                    print(i)
        -> Output: 
            0
            1
            2

-> Continue: The continue statement is used to skip the current iteration and move to the next iteration.
    -> Syntax: continue
    -> Example: for i in range(5):
                    if i == 3:
                        continue
                    print(i)
        -> Output: 
            0
            1
            2
            4

-> Pass: The pass statement is used to do nothing. It is essentially a placeholder.
    -> Syntax: pass
    -> Example: for i in range(5):
                    if i == 3:
                        pass
                    print(i)
        -> Output: 
            0
            1
            2
            3
            4

assert: The assert statement is used to check if a condition is true. If the condition is false, it raises an AssertionError.
    -> Syntax: assert <condition>
    -> Example: def check_age(age):
                    assert age >= 18, "Age must be greater than or equal to 18"
                    print("Age is valid")
                check_age(20)  -> Output: Age is valid
                check_age(16)  -> Output: AssertionError: Age must be greater than or equal to 18

'''