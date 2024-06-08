# Strings = it is data type that stores sequence of characters
# Escape Sequence character (tab= \t) (new line = \n)
"""str = "ishita\nradhe"
print(str)"""

# Concatenation
"""str1 = "ish"
str2 = "radhe"
final = str1+" "+str2
print(final)"""

# Length of string
# print(len(final))

# Indexing = can't modifying
"""str = "apna college"
print(str[0])"""


# Slicing = accessing parts of string  str[str_idx:end_idx] (end_idx not include)
"""str = "apna college"
print(str[0:4])   # last not include
print(str[5:len(str)])  
print(str[5:])   # ending index [5:len(str)]
print(str[:4])   # start index [0:4]
print(str[-3:-1])   # eg (-1 not include)
print(str[5])  # index number(ans = c)
print(str[0:4:2])   # start from 0, end to 3, skip 1
print(str[-2:])       # start from last(reverse) goes to -2
print(str[-9:-1])     # start from reverse(-1 nit include)
print(str[::-1])        # print reverse
print(str[::2])         # skip 1
print(str[::-2])        # skip 1 from reverse """


# String Function
"""str = "i am studying python from apna college"

print(str.endswith("ege"))  # returns True if string ends with substring
print(str.capitalize())     # capitalizes 1st char (doesn't change original string)
    # str = str.capitalize()   (for change the original string)
print(str.replace("python","js"),str.replace("o","a"))   # replace all occurrences of old
print(str.find("o"))        # returns 1st index of 1st word
print(str.count("a"))        # counts the occurrence of substring
print(str.isalnum())  # there is space in the string so its FALSE
print(str.isalpha())  # there is no ALFANUMERICAL so its FALSE
print(str.lower())
print(str.upper())"""



# practice = input user's 1st name & print length
"""name = input("enter name:")
print(name,len(name))"""


# find the occurrence of '$' in string
"""str = "i am $sign $19.99"
print(str.count("$"))"""



# Conditional Statement (if-elif-else)
"""light = "yellow"
if(light == "red"):
    print("stop")        # indentation (proper spacing)
elif(light == "yellow"):
    print("look")
else:
    print("go")"""
    


# Grade of student
"""marks = int(input("enter marks:"))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("Grade =",grade)"""


# Nesting
"""age = 98
if(age >= 18):
    if(age >= 80):
        print("can't drive")
    else:
        print("can drive")
else:
    print("can't drive")"""
    
    
# shorthand if-else
"""a = int(input("enter a:\n"))
b = int(input("enter b:\n"))
if a>b: print("A is greater")
print("A is greater") if a>b else print("B is greater")   """


# extra sololearn
"""weight = int(input("enter weight:"))
height = float(input("enter height:"))
bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
    print("under weight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi <30:
        print("over weight")
else:
    print("obesity") """ 
    


# check if a number by the user is odd or even
"""num = int(input("enter number:"))
if(num % 2 == 0):
    print("even")
else:
    print("Odd")"""



# find the greatest of 3 numbers entered by the user
"""a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))

if(a >= b and a >= c):
    print("1st is largest",a)
elif(b >= c):
    print("2nd is largest",b)
else:
    print("3rd is largest",c)"""
    
    

# check if a number is a multiple of 7 or not
"""num = int(input("enter number:"))
if(num % 7 == 0):
    print(num,"is multiply by 7")
else:
    print(num,"is not multiply by 7")"""
    


# Exercise-2 : Faulty calculator
# design a calculator which will correctly solve all problems except
# 45*3=555 , 56+9=77 , 56/6=4
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = input("what you want?=>" + " + , - , * , / , % ")

if num1==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1==56 and num2==6 and num3=='/':
    print("4")
elif num3 == '+':
    plus = num1 + num2
    print(plus)
elif num3 == '-':
    subtraction = num1 - num2
    print(subtraction)
elif num3 == '*':
    multi = num1 * num2
    print(multi)
elif num3 == '/':
    div = num1 / num2
    print(div)
elif num3 == '%':
    percent = num1 % num2
    print(percent)
else:
    print("enter right choice") 
