# Day - 15

'''
Lambda functions 
-> They are small anonymous functions defined with the lambda keyword.
-> They can take any number of arguments but can only have one expression.
        Syntax : lambda arguments : expression
        Example : add_ = lambda a,b,c : a+b+c
                  print(add_(20,50,30))          # Output : 100

        Example : num = 30 
                  num2 = 20
                  number = lambda num, num2 : num if num > num2 else num2
                  print(number(num,num2))        # Output : 30

-> filter: It will perform only on selected elements of iterables. 
        Syntax : filter(lambda arguments : expression, list/tuple/set)
        Example : numbers = [1,2,3,4,5]
                  even_number = list(filter(lambda num : num % 2 == 0, numbers))
                  print(even_number)              # Output : [2,4]

-> map: It will perform operations on all elements of iterables.
        Syntax : map(lambda arguments : expression, list/tuple/set)
        Example : numbers = [1,2,3,4,5]
                  square_number = list(map(lambda num : num**2, numbers))
                  print(square_number)            # Output : [1,4,9,16,25]
        Example : numbers = [1,2,3,4,5]
                  even_number = list(map(lambda num : num % 2 == 0, numbers))
                  print(even_number)              # Output : [False, True, False, True, False]

-> reduce: It will repeatedly applies a function to the elements and reduce them in one final value.
        Note: We have to import reduce() from functools module using "from functools import reduce".
        Syntax : reduce(lambda arguments : expression, list/tuple/set)
        Example : numbers = [1,2,3,4,5]
                  sum_number = reduce(lambda num1, num2 : num1 + num2, numbers)
                  print(sum_number)                # Output : 15     

'''

