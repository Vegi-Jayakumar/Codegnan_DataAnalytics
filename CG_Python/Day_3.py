#Day - 3

'''
Datatypes & TypeConversions
-> Data types are the types of data that can be stored in a variable.
-> Type Conversions are the conversions of data from one type to another.

Datatypes:
    1. Integer (int) : Whole numbers (positive or negative)
        Eg: 1, 45, 748, etc.
    2. Float (float) : Real numbers (numbers with decimal points)
        Eg: 1.0, 45.5, 748.9, etc.
    3. String (str) : Text (sequence of characters) that is inclosed in single quotes(''), double quotes(""), or triple quotes("""). It is immutable.
        Eg: "Hello", "123", "@*&", " ", etc.
    4. Boolean (bool) : Logical values. It can be True or False. It is immutable.
        Eg: True, False
    5. List (list) : It is a Collection of Ordered, mutable items. It can store different data types. It is represented by square brackets [] that are saperated by commas.
       Inside the list, we call them as items. We can access them using indexing starting from 0.
        Eg: [1, 2, 3, 4, 5], ["Hello", "World", "Python"], etc.
    6. Tuple (tuple) : It is a collection of Ordered, immutable items. It can store different data types. It is represented by parentheses () that are saperated by commas.
       Inside the tuple, we call them as items. We can access them using indexing starting from 0.
        Eg: (1, 2, 3, 4, 5), ("Hello", "World", "Python"), etc.
    7. Set (set) : It is a collection of Unordered unique items. It cannot accept any duplicate values. It can store different data types. It is mutable. It is represented by curly brackets {}.
       Inside the set, we call them as items. We cannot access them using indexing. The elements are saperated by commas.
        Eg: {1, 2, 3, 4, 5}, {"Hello", "World", "Python"}, etc.
    8. Dictionary (dict) : It is a collection of Unordered key:value pairs. It is represented by curly brackets {} and colon(:). It can store different data types. It is mutable.
       Inside the dictionary, we call them as key:value pairs or items and are saperated by commas. We can access them using keys.
       We use only immutable data type for keys and either immutable or mutable data types for values. 
        Eg: {"Name": "John", "Age": 30, "City": "New York", 30:"Thirty", (12,13):"Tuple"}
    9. NoneType (None) : Represents the absence of a value. It is immutable.
        Eg: None

Mutable:
-> Mutable datatypes are those whose values can be modified after creation.
-> List (list), Set (set), Dictionary (dict) are mutable.

Immutable:
-> Immutable datatypes are those whose values cannot be modified after creation.
-> Integer (int), Float (float), String (str), Boolean (bool), Tuple (tuple), NoneType (None) are immutable.

Type Conversion:
    -> Type Conversion is the process of converting a value from one data type to another.
    -> It is done using type conversion functions.
    -> There are two types of type conversion:
        1. Implicit Type Conversion : Conversion of data from one type to another automatically.
        2. Explicit Type Conversion : Conversion of data from one type to another manually.
   
        -> int() : Converts a value to an integer. float values and strings which contains integers can be converted to int. If the string is empty or contains any non-numeric characters, it will raise a ValueError.
        -> Eg: float --> int
           price = 49.99 
           print(int(price))   # Output: 49
        -> Eg: str --> int
           price = "49"
           print(int(price))   # Output: 49
        -> float() : Converts a value to a float.int values and strings which contains numbers can be converted to float. If the string is empty or contains any non-numeric characters, it will raise a ValueError.
        -> Eg: int --> float
           price = 49 
           print(float(price))   # Output: 49.0
        -> Eg: str --> float
           price = "49"
           print(float(price))   # Output: 49.0 
        -> str() : Converts a value to a string. int values and float values can be converted to strings.
        -> Eg: float -->str
           price = 49.99 
           print(str(price))   # Output: "49.99"
        -> Eg: int --> str
           price = 49
           print(str(price))   # Output: "49" 
        -> list() : Converts a value to a list. string can be converted to list. 
           Eg: str --> list
              name = "John"
              print(list(name))   # Output: ["J", "o", "h", "n"]
           Eg: tuple --> list
              name = ("John", "Jane", "Bob")
              print(list(name))   # Output: ["John", "Jane", "Bob"]
           Eg: set --> list
              name = {"John", "Jane", "Bob"}
              print(list(name))   # Output: ["John", "Jane", "Bob"]
           Eg: dict --> list
              name = {1: "John", 2: "Jane", 3: "Bob"}
              print(list(name))   # Output: [1, 2, 3] (only keys are converted to list)
              
        -> tuple() : Converts a value to a tuple. string can be converted to tuple.
           Eg: str --> tuple
              name = "John"
              print(tuple(name))   # Output: ("J", "o", "h", "n")
           Eg: list --> tuple
              name = ["John", "Jane", "Bob"]
              print(tuple(name))   # Output: ("John", "Jane", "Bob")
        -> set() : Converts a value to a set. string can be converted to set.
           Eg: str --> set
              name = "John"
              print(set(name))   # Output: {"J", "o", "h", "n"}
           Eg: list --> set
              name = ["John", "Jane", "Bob"]
              print(set(name))   # Output: {"John", "Jane", "Bob"}
        -> dict() : Converts a value to a dictionary. It can only convert list of tuples or list of strings to dictionary. If the list of strings are in key:value format, it will convert to dictionary.
           Eg: list of tuples --> dict
              name = [("John", 1), ("Jane", 2), ("Bob", 3)]
              print(dict(name))   # Output: {"John": 1, "Jane": 2, "Bob": 3}
           Eg: list of strings --> dict
              name = ["John", "Jane", "Bob"]
              print(dict(name))   # Output: {"John": 1, "Jane": 2, "Bob": 3}



'''
