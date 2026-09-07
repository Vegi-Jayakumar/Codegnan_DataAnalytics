#Day - 7

'''
List
-> Collection of different data types that are saperated by commas and enclosed in square brackets.
    *Syntax: list_name = [element1, element2, element3, ..., elementn]
    *Example: my_list = [1, 2, 3, 4, 5]

List Operations
-> Indexing: Accessing elements of a list using their index.
    *Syntax: list_name[index]
    *Example: my_list = [1,2,3,4,'Python']
              print(my_list[2])        #output : 3
              print(my_list[4])        #output : 'Python'
              print(my_list[4][2])     #output : 't'
              all_ = [12,[1,"Python",[1,4],(78,[6,7])],['Java',78]]
              print(all_[1][3][1])     #output : [6,7]
              print(all_[1][-1][1][1]) #output : 7

-> Length: Gives the number of elements in a list.
    *Syntax: len(list_name)
    *Example: my_list = [1,2,3,4,'Python']
              all_ = [12,[1,"Python",[1,4],(78,[6,7])],['Java',78]]
              print(len(my_list))       #output : 5
              print(len(all_))          #output : 3
              print(len(all_[1]))       #output : 4

-> Slicing: Extracting a portion of a list.
    *Syntax: list_name[start:end]
    *Example: my_list = [1,2,3,4,'Python']
              print(my_list[0:2])     #output : [1,2]
              print(my_list[2:4])     #output : [3,4]
              print(my_list[0:4:2])   #output : [1,3]

-> Concatenation: Joining two or more lists.
    *Syntax: list_name1 + list_name2
    *Example: my_list = [1,2,3,4,'Python']
              all_ = [12,[1,"Python",[1,4],(78,[6,7])],['Java',78]]
              print(my_list + all_)   #output : [1,2,3,4,'Python',[12,[1,"Python",[1,4],(78,[6,7])],['Java',78]]]

Methods
-> append() : Adds a new item to the end of the list.
    *Syntax: list_name.append(item)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.append('World')
              print(my_list)        #output : [1,2,3,4,'Python','World']

-> extend() : Adds all the items of an iterable (tuple, string, list, set, dictionary) to the end of the list.
    *Syntax: list_name.extend(iterable)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.extend(['World',1,2,3])
              print(my_list)        #output : [1,2,3,4,'Python','World',1,2,3]

-> insert() : Inserts an item at a specific position in the list.
    *Syntax: list_name.insert(index, item)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.insert(2,'World')
              print(my_list)        #output : [1,2,'World',3,4,'Python']

-> remove() : Removes the first occurrence of a specific value from the list.
    *Syntax: list_name.remove(value)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.remove(2)
              print(my_list)        #output : [1,3,4,'Python']

-> pop() : Removes and returns the item at a specific position (default: last item) it is based on index value.
    *Syntax: list_name.pop(index)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.pop()
              print(my_list)        #output : [1,2,3,4]
              my_list.pop(2)
              print(my_list)        #output : [1,2,4]

-> del : Deletes an item or a slice from the list.
    *Syntax: del list_name[index]
    *Example: my_list = [1,2,3,4,'Python']
              del my_list[2]
              print(my_list)        #output : [1,2,4,'Python']

-> clear() : Removes all items from the list.
    *Syntax: list_name.clear()
    *Example: my_list = [1,2,3,4,'Python']
              my_list.clear()
              print(my_list)        #output : []

-> copy() : Returns a shallow copy of the list.
    *Syntax: list_name.copy()
    *Example: my_list = [1,2,3,4,'Python']
              my_list.copy()
              print(my_list)        #output : [1,2,3,4,'Python']

-> count() : Returns the number of occurrences of a specific value in the list.
    *Syntax: list_name.count(value)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.count(2)
              print(my_list)        #output : 1

-> index() : Returns the index of the first occurrence of a specific value in the list.
    *Syntax: list_name.index(value)
    *Example: my_list = [1,2,3,4,'Python']
              my_list.index(2)
              print(my_list)        #output : 1

-> reverse() : Reverses the order of items in the list.
    *Syntax: list_name.reverse()
    *Example: my_list = [1,2,3,4,'Python']
              my_list.reverse()
              print(my_list)        #output : ['Python',4,3,2,1]








'''

my_list = [1,2,3,4,'Python']

print(my_list)