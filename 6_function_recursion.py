# Function = block of statement that perform a specific task
"""def calcSum(a, b):   # function definition(parameters)
    return a + b    
sum = calcSum(3, 2)   # function call (argument)
print(sum)"""


# avg of 3 num
"""def average(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
average(1, 2, 3)
average(90, 85, 80)   """



# Built-in Function = print(), len(), type(), range()
# User-defined FUnction

# default parameter = assigning a default value to parameter, which is used when no argument passed
"""def cal_prod(a=1, b=1):
    print(a * b)
    return a * b
cal_prod() """



# print length of list(list is parameter)
"""cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]
print(heroes[0])
def print_len(list):
    print(len(list))
print(len(heroes))
print(len(cities)) 


# print element of list in single line.(list is parameter)
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heroes)
print_list(cities)"""


# find factorial of n(n is parameter)
"""def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)"""


# covert USD to INR
"""def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD=",inr_val,"INR")
converter(100)"""


# odd even
"""def odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
odd_even(25)"""


# search engine  sololearn
"""def search(text,word):
    if word in text:
        print("word found")
    else:
        print("word not found")
text = input("enter text:")
word = input("enter word:")
search(text,word)   """   
   



# Recursion = when a function calls itself repeatedly
"""def show(n):
    if(n == 0):   # base case
        return
    print(n)
    show(n-1)
    print("end")
show(5)"""

# factorial
"""def fact(n):
    if(n == 1 or n ==0):
        return 1
    return fact(n-1) * n
print(fact(5))"""



# recursive function to calculate sum of 1st n natural numbers
"""def cal_sum(n):
    if (n == 0):
        return 0
    return cal_sum(n-1) + n
sum = cal_sum(10)
print(sum)"""


# recursive function to print all element in list.(list & index as parameter)
"""def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
list = ["a", "b", "c", "d"]
print_list(list)"""


# fibonacci
"""def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("enter number:"))
print(fibonacci(number)) """  
