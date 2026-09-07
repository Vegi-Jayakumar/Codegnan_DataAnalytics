# Day - 16

'''
List Comprehension
-> it is a way to create a new lists based on the existing iterables in a concise way.
-> syntax : [expression for item in iterable]
-> syntax : [expression for item in iterable if condition]
-> syntax : [expression if-else condition for item in iterable]

-> Example :
    num = [i for i in range(5)]
    print(num)                     # Output : [0,1,2,3,4]

    old_list = [1,2,3,4,5,6,7,8,9,0]
    num = [i for i in old_list if i % 2 == 0 ]
    print(num)                     # Output : [2,4,6,8,0]
    new_ = [i if i % 2 == 0 else "none" for i in old_list]
    print(new_)                    # Output : ["none", 2, "none", 4, "none", 6, "none", 8, "none", 0]
 

Nested List Comprehension:
-> when we use one list comprehension inside another list comprehension, it is called nested list comprehension.
-> syntax : [[expression for item in iterable] for item in iterable]
-> Example : 
    mat = [[i*j for i in range(1,6)]for j in range(1,10)] 
    print(mat)                      # Output : [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15], [4,8,12,16,20], [5,10,15,20,25]]

    mat_ = [[1,2,3],[4,5,6],[7,8,9]]
    list = [num for row in mat_ for num in row]
    print(list)                    # Output : [1,2,3,4,5,6,7,8,9]  

Generators:
-> Generators are used to generate a sequence of values(one value at a time).
-> Syntax : def generator_name():
    yield value
-> Example : 
    def num_generator():
        yield 1
        yield 2
        yield 3
    gen = num_generator()
    print(next(gen))                    # Output : 1
    print(next(gen))                    # Output : 2
    print(next(gen))                    # Output : 3

    def name_generator():
        names = ['Jayakumar','praveen','sanjay']
        for name in names:
            yield name

    name = name_generator()
    print(next(name))
    print(next(name)) 
    print(next(name))

'''


