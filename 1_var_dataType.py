# Translator = compiler / Interpreter
# Simple,Easy..free,open source..High level lang..develop by Guido Van Rossum.. Portable

# print("hello","ishita",8+11)

# Variable = it is a name given to a memory location in a program
# Data Type = Integer, String, Float, Boolean, None
name = "radhe"
age = 20
weight = 42.5
old = False
a = None
print("my name is",name ,"age is",age)
print(type(name))
print(type(age))
print(type(weight))
print(type(old))
print(type(a))   


# Keywords = are reserved words in Python

# Operators = it is a symbol that performs a certain operation between operands.
# Arithmetic Operators (+  -  *  /  %  **)
"""a = 5
b = 2
print(a%b)   # remainder
print(a**b)  # a^b"""

# Relational/Comparison (==  !=  >  <  >=  <=)  (True or False )

# Assignment Operator (=  +=  -=  *=  /=  %=  **=)
"""num = 10
num += 10   #num = num + 10
print(num)"""

# Logical Operator (not,and,or)(boolean)
# not False = True .... not True = False
# and = both True 
# or = atleast one true

# identity operator :- is, is not
"""a = True
b = False
print(a is b)
print(a is not b)"""

# membership operator:- in, not in
"""list=[3,4,5,7,8,9,17]
print(8 in list)
print(25 in list)
print(25 not in list) """    

# bitwise operator   & |
"""print(0 & 1)  # and  0
print(0 | 1)   # or  1"""


# Type Conversion = automatically done by Python
"""a = 2
b = 4.25
print("sum =",a+b)  # convert int into float"""

# Type Casting = manually done by user
"""a = float("2")
b = 4.25
print(a+b)"""


# input()
"""name = input("enter name=")
print("welcome",name)"""



# Practice = program to input 2 numbers & print their sum
"""num1 = float(input("enter num1 ="))
num2 = float(input("enter num2 ="))
print("sum =",num1 + num2)"""


# WAP to input side of a square & print area.
"""side = float(input("enter side="))
print("area of square=",side*side)  #side**2"""


# input 2 floating point number & print their avg
"""f1 = float(input("enter num="))
f2 = float(input("enter num="))
print("avg=",(f1+f2)/2)"""


# input 2 int nums,a,b. Print true if a is greater or equal to b. if not print false.
"""a = int(input("enter 1st="))
b = int(input("enter 2nd="))
print(a >= b)"""
