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

Slicing --> [start:stop]       #Start is included and end is excluded; Step is optional
batch[0:3]          #Output: ['name','python','Swift']
batch[4:6]          #Output: ['C++','C']
batch[-3:]          #Output: ['C++','C','Data Science']

Striding --> [start:stop:step]
batch[::2]          #Output: ['name','Swift',['C++','C','Data Science'], 'C++']
batch[::3]          #Output: ['name','Java','c']
batch[1:5:2]        #Output: ['python','Java']

#Tryout in notes with explanation
print(batch[:7:4])       #Output: ['name',['C++','C','Data Science']]
print(batch[7::4])       #Output: ['Data Science']
print(batch[1::5])       #Output: ['python','C']
print(batch[1:7:-2])     #Output: []
print(batch[-1:-4:-1])   #Output: ['Data Science', 'C', 'C++']

batch = ['name','python','Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']
batch.insert(2,('HTML','CSS','Javascript'))
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','Data Science'], 'C++','C','Data Science']

sub-indexing
print(batch[2][0:2])    #Output: ('HTML', 'CSS')
print(batch[2][1])      #Output: 'CSS'
print(batch[2][::2])    #Output: ('HTML', 'Javascript')

index position
print(batch[2].index('HTML'))           #Output: 0
print(batch[2].index('CSS'))            #Output: 1
print(batch[2].index('Javascript'))     #Output: 2
print(batch[2].index('java'))           #Output: ValueError
print(batch[2].count('java'))           #Output: 0

#Convert string into uppercase
batch[5][2] = batch[5][2].upper()
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE'], 'C++','C','Data Science']

#Insert element in sub-list
batch[5].append('Python')
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C++','C','Data Science']

#Removing Elements -->remove(value),pop(index),clear()

batch.remove('C++')
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C','Data Science']
batch[2].pop()
print(batch)        #Output: AttributeError
del batch[2][1]     #Output: TypeError

#concatinating a tuple
batch[2] = batch[2]+('Jsp',)
print(batch)        #Output: ['name','python',('HTML','CSS','Javascript','Jsp'),'Swift','Java', ['C++','C','DATA SCIENCE','Python'], 'C','Data Science']

#Dictionaries --> {k:v}, keys must be unique, they can be int, str, float, list
P_lang = {}
P_lang['Frontend'] = ['html','css','js']
P_lang['Backend'] = ['py','nodejs','expressjs']
P_lang['Database'] = ['mysql','mongodb','postgresql']
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql']}

#update dictionary --> dict_1.update(dict_2)
P_lang.update({'Frameworks':['react','angular','vue'],
               'Tools':('github','IDE')})
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql'], 'Frameworks': ['react', 'angular', 'vue'], 'Tools': ('github', 'IDE')}

#keys in dictionary
print(P_lang.keys())       #Output: dict_keys(['Frontend', 'Backend', 'Database', 'Frameworks', 'Tools'])

#add values to keys is a dictionary
P_lang['Frameworks'].append('React Native')
print(P_lang)       #Output: {'Frontend': ['html', 'css', 'js'], 'Backend': ['py', 'nodejs', 'expressjs'], 'Database': ['mysql', 'mongodb', 'postgresql'], 'Frameworks': ['react', 'angular', 'vue', 'React Native'], 'Tools': ('github', 'IDE')}

#Tasks to be done
create a dictionary using codegnan portal as example. keys:Exams,Mock Interviews, Project Demos.
push to github --> share your link in whatsapp group.

'''
