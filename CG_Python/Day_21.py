# Day - 19

'''
Exception Handling
-> This is the way of handling errors in a program.
-> syntax:  try:
                program
            except error_type:
                Error handling code
            else:
                program if no error
            finally:
                program

->Note: We can write any number of except conditions for one code written in the try block.
->Note: We can only write one try block.

-> Try:
    * The try block, where we can write the code which may contain errors or exceptions.

-> Except:
    * The except block, where we can write the code to handle the errors or exceptions.

-> Else:
    * The else block, where we can write the code to be executed if there are no errors or exceptions.

-> Finally:
    * The finally block, where we can write the code to be executed regardless of whether there are errors or exceptions or not.

File Handling
-> This is the way of handling files in Python.
-> It is an object, which is used to create, update, read, and delete the contents of a file.
-> syntax:  file = open("filename", "mode") or with open("filename", "mode") as file:
    * The file created using the 'with' keyword is automatically closed after the program is executed.

-> modes:   "r"  - read
            "w"  - write
            "a"  - append
            "x"  - create
            "r+" - read and write
            "w+" - write and read
            "a+" - append and read

-> We can open a file in binary mode by adding "b" to the mode. e.g., "rb", "wb", "ab", "r+b", "w+b", "a+b"

->function:
    -> Syntax for reading a file:
        * file.read() - reads the entire file
        * file.readline() - reads one line at a time
        * file.readlines() - reads all lines at a time

    -> Syntax for writing to a file:
        * file.write(data) - overwrites existing data to the file

    -> Syntax for appending to a file:
        * file.write(data) - appends data to the file

    -> Syntax for closing a file:
        * file.close() - closes the file

'''
