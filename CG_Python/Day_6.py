#Day - 6

'''
String Operations
-> Indexing : Accessing individual characters in a string.
    * Positive Indexing : Starts from the beginning of the string. It's first value is 0.
    * Negative Indexing : Starts from the end of the string. It's first value is -1.
    * Syntax: Variable_name[Index_value]
    * Example: 
        string = "Hello"
        print(string[0])  # Output: H
        print(string[-1]) # Output: o

-> Slicing : Accessing a range of characters (particular part of string) in a string.
    * Syntax: Variable_name[Start_index:End_index:Step_value]
    * Example: 
        string = "Hello"
        print(string[0:2])   # Output: He
        print(string[1:3])   # Output: el
        print(string[:2])    # Output: He
        print(string[2:])    # Output: llo
        print(string[0:5:2]) # Output: Hlo
        print(string[::-1])  # Output: olleH

-> Length : It is a built-in function, used to find out the total number of characters in the string.
    * Syntax: len(Variable_name)
    * Example: 
        string = "Hello"
        print(len(string))  # Output: 5

-> Upper : It is a built-in function, used to convert the string into uppercase.
    * Syntax: Variable_name.upper()
    * Example: 
        string = "Hello"
        print(string.upper()) # Output: HELLO

-> Lower : It is a built-in function, used to convert the string into lowercase.
    * Syntax: Variable_name.lower()
    * Example: 
        string = "Hello"
        print(string.lower()) # Output: hello

-> Index : It gives the index of the first occurrence of the given value.
    * Syntax: Variable_name.index(substring , start_index, end_index)
    * Note: Start_index and end_index are optional.
    * Example: 
        string = "Hello world"
        print(string.index("o"))    # Output: 4
        print(string.index("o", 5)) # Output: 7

-> Replace : It replaces the old substring with the new substring.
    * Syntax: Variable_name.replace(Old_substring, New_substring)
    * Example: 
        string = "Hello world"
        print(string.replace("world", "Python")) # Output: Hello Python

-> Split : It is a built-in function, used to split the string into a list of strings.
    * Syntax: Variable_name.split(Separator)
    * Note: Separator is optional. If not given, it will split by space.
    * Example: 
        string = "Hello world"
        print(string.split(" ")) # Output: ['Hello', 'world']

-> Join : It is a built-in function, used to join the list of strings into a string.
    * Syntax: Separator.join(List_of_strings)
    * Note: Separator is optional. If not given, it will join by space.
    * Example: 
        list_of_strings = ["Hello", "world"]
        print(" ".join(list_of_strings)) # Output: Hello world

-> Count : It is a built-in function, used to find out the total number of occurrences of the given substring.
    * Syntax: Variable_name.count(substring, start_index, end_index)
    * Note: Start_index and end_index are optional.
    * Example: 
        string = "Hello world"
        print(string.count("l"))      # Output: 3
        print(string.count("o", 5))   # Output: 1

'''
