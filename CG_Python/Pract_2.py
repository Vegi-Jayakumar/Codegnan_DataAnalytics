#print even or odd till range
# limit_ = int(input("Enter the limit: "))
# for i in range(limit_):
#     if (i+1) % 2 == 0:
#         print(f"{i+1} is Even")
#     else:
#         print(f"{i+1} is Odd")

#print only odd numbers
# limit_ = int(input("Enter the limit: "))
# for i in range(limit_):
#     if (i+1) % 2 != 0:
#         print(f"{i+1}")

#specify even or odd in a list
# nums = [23, 78, 97, 5]
# for i in nums:
#     if i % 2 == 0:
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd")

#find number of vowels in a string
# words_ = input("Enter the string: ")
# sum = 0
# for i in words_:
#     if i.lower() in 'aeiou':
#         sum += 1
# print(f"number of vowels in the string is: {sum}")

#find the number of consonants
# words_ = input("Enter the string: ")
# sum = 0
# for i in words_:
#     if i.lower() not in 'aeiou ':
#         sum += 1
# print(f"number of consonants in the string is: {sum}")

#removing duplicates from the list
# nums = [1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
# new_nums = []
# for i in nums:
#     if i not in new_nums:
#         new_nums.append(i)
# print(new_nums)

#find the duplicate values in a tuple
# nums = (1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10)
# new_nums = []
# dup_nums = []
# for i in nums:
#     if i not in new_nums:
#         new_nums.append(i)
#     else:
#         dup_nums.append(i)
# print(f"Duplicate numbers are: {tuple(dup_nums)}")

#count the number of words in a string
# words_ = input("Enter the string: ")
# new_words_ = words_.split()
# print(len(new_words_))
