# Day - 22

'''
Tokens: Keywords,variables,operators,punctuations,Literals

variables should not start with number, spaces, & any other symbols other than underscore.

batch = ['name','python']
print(batch)        # Output: ['name','python']
print(type(batch))  #everything is an object (POP --> OOP)      # Output: <class 'list'>

len() --> returns the numbr of items in a collection

print(len(batch))   # Output: 2

Add 3 more student names into it
List --> Collection --> append(),extend(),insert()

batch.append('Java')
print(batch)         # Output: ['name','python','Java']
batch.append(['C++','C','Data Science'])
print(batch)         # Output: ['name','python','Java',['C++','C','Data Science']]
batch.extend(['C++','C','Data Science'])
print(batch)         # Output: ['name','python','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
batch.insert(2,'Swift') #inserts given value at specific index for positive index and before the specified index for negative index.
print(batch)         # Output: ['name','python','Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
print(len(batch))    # Output: 7

Indexing --> positive index --> from left to right --> starts with 0 and ends with len(obj)-1
             negative index --> from right to left --> starts with -1 and ends with -len(obj)

batch[0] --> 'name'
batch[1] --> 'python'
batch[-1] --> 'C'
batch[-2] --> 'C++'
batch[35] --> IndexError

Slicing --> [start:stop:step]       #Start is included and end is excluded; Step is optional
batch[0:3]          #Output: ['name','python','Swift']
batch[4:6]          #Output: ['C++','C']
batch[-3:]          #Output: ['C++','C','Data Science']

Striding
batch[::2]          #Output: ['name','Swift',['C++','C','Data Science'], 'C++']
batch[::3]          #Output: ['name','Java','c']
batch[1:5:2]        #Output: ['python','Java']

#Tryout in notes with explanation
print(batch[:7:4])       #Output: ['name',['C++','C','Data Science']]
print(batch[7::4])       #Output: ['Data Science']
print(batch[1::5])       #Output: ['python','C']
print(batch[1:7:-2])     #Output: []
print(batch[-1:-4:-1])   #Output: ['Data Science', 'C', 'C++']

'''
