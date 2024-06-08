# string " "= immutable (can't change)..can access value by index but can't change
# tuple ()= immutable
# set {}= mutable
# lists []= mutable (can change)
# Dictionary {}= mutable


# Lists[] = built-in data type that stores set of value (integer, float, string)
"""marks = [94.4, 90.3, 50.7, "ish", 70]
print(type(marks))
print(marks[0])
print(len(marks))
marks[3] = "radhe"
print(marks)"""


# List Slicing  (similar to string slicing)
"""marks = [85, 94, 76, 63, 48]
print(marks[1:4])     # last index can't include
print(marks[-3:-1])   # negative index"""


# List Methods
"""list = [2, 1, 3]
list.append(4)             # adds one element at the end
list.sort()                # sorts in ascending order
list.sort(reverse=True)    # sorts in descending order
list.reverse()             # reverse list
list.insert(1, 5)          # insert element at index (idx, el)
list.remove(1)             # remove 1st occurrence of element
list.pop(2)                # remove element at index (idx)
print(list)"""



# Tuple(immutable) = built-in data type that lets us create Immutable sequence of values
"""tuple = (2, 1, 3, 4)
print(tuple[0])
print(tuple[1:3])"""


# Tuple Methods 
"""tup = (1, 2, 3, 4)
print(tup.index(4))       # returns index number of first occurrence
print(tup.count(2))       # counts total occurrence"""


# WAP to ask user to enter name of 3 fav movies & store them in list
"""movies = []
m1 = input("enter movie 1:")
m2 = input("enter movie 2:")
m3 = input("enter movie 3:")
movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)"""


# WAP to check if a list contains palindrome of element.(use copy() method)
"""l1 = [1, 2, 1]
l2 = [1, 2, 3]
copy_l1 = l1.copy()
copy_l1.reverse()

if(copy_l1 == l1):
    print("palindrome")
else:
    print("not palindrome")"""
    
    

# WAP to count number of student with "A" grade in the following tuple
"""grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))"""


# store above value in list & sort them from "A" to "D".
"""grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)"""