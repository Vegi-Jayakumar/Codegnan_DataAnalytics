#Day - 9

'''
set operations:
-> Indexing: It is used to access elements in a set.
    Syntax: set[index]
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             print(data[0])  # Output = 1
             print(data[-1]) # Output = 5

-> Slicing: It is used to access a range of elements in a set.
    Syntax: set[start:end]
    Example: data = {1,2,3,4,5}
            print(data[0:2]) # Output = {1,2}

-> Union: It is used to combine two sets
    Syntax: set1 | set2 or set1.union(set2)
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             print(data | nums)      # Output = {1,2,3,4,5,6}
             print(data.union(nums)) # Output = {1,2,3,4,5,6}

-> intersection: It is used to find the common elements in two sets.
    Syntax: set1 & set2 or set1.intersection(set2)
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             print(data & nums)             # Output = {4,5}
             print(data.intersection(nums)) # Output = {4,5}

-> Difference: It is used to find the elements in the first set but not in the second set.
    Syntax: set1 - set2 or set1.difference(set2)
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             print(data - nums)             # Output = {1,2,3}
             print(data.difference(nums))   # Output = {1,2,3}

-> Symmetric Difference: It is used to find the elements that are in either of the sets, but not in both.
    Syntax: set1 ^ set2 or set1.symmetric_difference(set2)
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             print(data ^ nums)                       # Output = {1,2,3,6}
             print(data.symmetric_difference(nums))   # Output = {1,2,3,6}

Set Methods:
-> addition: It is used to add a single element to a set.
    Syntax: set.add(element)
    Example: data = {1,2,3,4,5}
             data.add(6)
             print(data) # Output = {1,2,3,4,5,6}

-> update: It is used to add multiple elements to a set.
    Note: the elements should be in an iterable data type.
    Syntax: set.update([elements]) or set_1.update(set_2)
    Example: data = {1,2,3,4,5}
             nums = {4,5,6}
             data.update([7,8,9])
             print(data) # Output = {1,2,3,4,5,7,8,9}
             data.update(nums)
             print(data) # Output = {1,2,3,4,5,6,7,8,9}

-> remove: It is used to remove a specific element from a set.
    Note: If the element is not found, it will raise an error.
    Syntax: set.remove(element)
    Example: data = {1,2,3,4,5}
             data.remove(4)
             print(data) # Output = {1,2,3,5}
             data.remove(10)
             print(data) # Output = Error

-> discard: It is used to remove a specific element from a set.
    Note: If the element is not found, it will not raise an error.
    Syntax: set.discard(element)
    Example: data = {1,2,3,4,5}
             data.discard(3)
             print(data) # Output = {1,2,4,5}
             data.discard(10)
             print(data) # Output = {1,2,4,5}

-> clear: It is used to remove all the elements from a set.
    Syntax: set.clear()
    Example: data = {1,2,3,4,5}
             data.clear()
             print(data) # Output = set()



'''