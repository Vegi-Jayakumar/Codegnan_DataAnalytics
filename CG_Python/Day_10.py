#Day - 10

'''
Dictionary: 
- It is a collection of key:value pairs.
- It is mutable.
- It is ordered.
- Key must be unique and immutable.
- Value can be of any type.

Example: dict = {"name": "John", "age": 30, "city": "New York", 1: 2, (1,2): [1,2]}
                print(dict)  # Output = {"name": "John", "age": 30, "city": "New York", 1: 2, (1,2): [1,2]}

-> Accessing values: We can access values using keys.
    -> Syntax = dictionary_name[key_name] or dictionary_name.get(key_name)
    -> If the key is not found, it will raise a KeyError.
    -> get() method is also used to access the values of the dictionary. If key is not found, it will return None.
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                print(data_["address"])  # Output = {"Street": "123", "City": "Indore", "State": "MP"}
                print(data_.get("cgpa")) # Output = 8.5
                print(data_.get("phone")) # Output = None
                print(data_["phone"]) # Output = KeyError

-> changing/adding values in dictionary:
    -> We can change the values of the dictionary.
    -> update(): it is used to update the values of the specified key in a dictionary. If the key is not present inside the dictionary, then it will add the new key-value pair in the dictionary.
    -> Syntax = dictionary_name[key_name] = value or dictionary_name.update({key: value})
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                data_["phone"] = 1234567890
                data_["name"] = "shyam"
                print(data_) # Output = {"name": "shyam", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5, "phone": 1234567890}
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                data_.update({"phone": 1234567890})
                data_.update({"name": "Mohit"})
                print(data_) # Output = {"name": "Mohit", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5, "phone": 1234567890}

-> items(): it is used to return the values of the specified key in a dictionary.
    -> Syntax = dictionary_name.items()
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                print(data_.items()) # Output = dict_items([('name', 'Rahul'), ('age', 22), ('address', {'Street': '123', 'City': 'Indore', 'State': 'MP'}), ('cgpa', 8.5)])

-> keys(): it is used to return the values of the specified key in a dictionary.
    -> Syntax = dictionary_name.keys()
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                print(data_.keys()) # Output = dict_keys(['name', 'age', 'address', 'cgpa'])

-> values(): it is used to return the values of the specified key in a dictionary.
    -> Syntax = dictionary_name.values()
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                print(data_.values()) # Output = dict_values(['Rahul', 22, {'Street': '123', 'City': 'Indore', 'State': 'MP'}, 8.5])

-> clear(): it is used to remove all the items from the dictionary.
    -> Syntax = dictionary_name.clear()
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                data_.clear()
                print(data_) # Output = {}  

-> del: it is used to remove the items from the dictionary.
    -> Syntax = del dictionary_name[key_name]
    -> example: data_ = {"name": "Rahul", "age": 22,"address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}
                del data_["age"]
                print(data_) # Output = {"name": "Rahul", "address": {"Street": "123", "City": "Indore", "State": "MP"}, "cgpa": 8.5}

Statements: statements are used to perform operations.
-> Conditional Statements:
    -> if
    -> elif
    -> else
-> Iterative Statements or Loops:
    -> for
    -> while
-> Jump Statements or control Statements:
    -> break
    -> continue
    -> pass

Conditional Statements:
-> if: it is used to check if the condition is true and execute the statements if the condition is true.
    -> Syntax = if condition:
                    Statements
    -> example: if 10 > 5:
                    print("10 is greater than 5")

-> if-else: it is used to check if the condition is false and execute the code if the condition is false.
    -> Syntax = if condition:
                    statement_1
                else:
                    statement_2
    -> example: if 10 < 5:
                    print("10 is greater than 5")
                else:
                    print("10 is less than 5")

'''