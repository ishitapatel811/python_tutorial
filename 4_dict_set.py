# Dictionary = are used to store data value in key:value pair.
# they are unordered(not index), mutable(change) & don't allow duplicate keys
"""dict ={
    "name" : "ish",
    "learn" : ["python", "c", "js"],
    "topic": ("dict", "set"),
    "age": 21,
    "is_adult": True,
    "marks": 80.5
}
print(type(dict))
print(dict["name"])
dict["name"] = "radhe"       # can change
dict["surname"] = "patel"    # can add
print(dict)

null_dict = {}"""


# Nested Dictionaries
"""student = {
    "name" : "radhe",
    "subjects":{
        "phy": 90,
        "ch": 80,
        "math":85
    }
}
print(student["subjects"]["math"])"""



# Dictionary Method
"""dict ={
    "name" : "ish",
    "learn" : ["python", "c", "js"],
    "topic": ("dict", "set"),
    "age": 21,
    "is_adult": True,
    "marks": 80.5
}
print(list(dict.keys()))       # returns all keys
print(list(dict.values()))     # returns all value
print(dict.items())            # returns all (key, value) pairs as tuple
print(dict.get("name"))        # returns the key according to value
new = {"city" : "unjha"}       # inserts the specified items to the dictionary
dict.update(new)
print(dict)"""



# Set = it is collection of the unordered items
# each element in the set must be unique & mutable
# duplicate value can't count in set
"""coll = {1, 2, 3, 4, "ish"}
print(type(coll))
empty = set()   # empty set
print(type(empty))"""


# SET methods
"""col = set()
col.add(1)          # adds element
col.add(2)
col.remove(1)       # remove element
col.clear()         # empties the set
col.pop()           # removes random value
print(col)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))           # combines both set value & returns new
print(set1.intersection(set2))    # combines common values & returns new """



# store following meaning in python dictionary
"""dict = {
    "cat" : "small animal",
    "table" : ["piece of furniture", "list of facts & figures"]
}
print(dict)"""


# given list of subjects for students.Assume one classroom is required for 1 subject.
# how many classroom are needed by all students.
"""sub = {
    "python", "java", "c++", "python", "js", "java", "python", "java","c++","c"
}
print(len(sub))   # avoid duplicate value"""



# WAP to enter marks of 3 students from user& store them in dictionary. start with empty dict.
# add one bt one. use subject name as key & marks as value
"""marks = {}
x = int(input("enter phy:"))
marks.update({"phy" : x})
x = int(input("enter math:"))
marks.update({"math" : x})
x = int(input("enter chem:"))
marks.update({"chem" : x})
print(marks)"""



# figure out a way to store 9 & 9.0 as separate values in set.(help of built-in data type)
"""value = {
    ("float",9.0),
    ("int", 9)
}
print(value)"""
