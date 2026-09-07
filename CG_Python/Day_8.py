#Day - 8

'''
tuples 
    *they are nothing but the list but immutable.
    *we can pass a tuple value and that can be assigned to the variables, but should match same number of variables and values inside the tuple.
    *syntax: tuple_name = (Items separated by commas)
    *example: mytuple = (1, 2, 3, 4, 'Python')
    *example: name, age, batch = ('Jayakumar', 22, 'DA-006')

Tuple Operations:
-> indexing: it is used to access individual items in a tuple
        *syntax: mytuple[index]
        *example: mytuple[0]  # Output: 1
        *example: mytuple[4]  # Output: 'Python'
        *example: mytuple[-1] # Output: 'Python'

-> index: it is used to find the index of an item in a tuple
        *if the item is not found in the tuple, it will raise ValueError(it will give 0 if index is not found)
        *syntax: mytuple.index(item)
        *example: mytuple.index(1)        # Output: 0
        *example: mytuple.index('Python') # Output: 4

-> Length: it is used to find the length of a tuple(number of items in a tuple)
        *syntax: len(tuple_name)
        *example: len(mytuple)  # Output: 5

-> Max: it is used to find the maximum value in a tuple
        *all the items in the tuple should be of same data type
        *syntax: max(tuple_name)
        *example: mytuple2 = (1, 2, 3, 4, 5)
                  max(mytuple2)  # Output: 5

-> Min: it is used to find the minimum value in a tuple
        *all the items in the tuple should be of same data type
        *syntax: min(tuple_name)
        *example: mytuple2 = (1, 2, 3, 4, 5)
                  min(mytuple2)  # Output: 1

-> count: it is used to find the count of an item in a tuple
        *syntax: mytuple.count(item)
        *example: mytuple.count(1)         # Output: 1
        *example: mytuple.count('Python')  # Output: 1

-> concatenation: it is used to join two or more tuples
        *syntax: tuple1 + tuple2 + ...
        *example: mytuple_1 = (1, 2, 3)
        *example: mytuple_2 = (4, 5, 6)
        *example: mytuple_1 + mytuple_2  # Output: (1, 2, 3, 4, 5, 6)

-> slicing: it is used to access a range of items in a tuple
        *syntax: mytuple[start:end:step]
        *example: mytuple[0:3]    # Output: (1, 2, 3)
        *example: mytuple[1:4:2]  # Output: (2, 4)

-> Sort: it is used to sort the items in a tuple
        *all the items in the tuple should be of same data type
        *syntax: sorted(tuple_name, reverse = True)
        *example: mytuple2 = (4, 2, 1, 5, 3)
                  sorted(mytuple2)                  # Output: (1, 2, 3, 4, 5)
                  sorted(mytuple2, reverse = True)  # Output: (5, 4, 3, 2, 1)

'''