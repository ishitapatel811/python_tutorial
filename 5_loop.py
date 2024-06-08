# Loop = loops are used to repeat instructions
# while loop

# print numbers from 1 to 100
"""i = 1
while i <= 100:
    print(i)
    i += 1"""
    
# print 100 to 1
"""i = 100
while i >= 1:
    print(i)
    i -= 1"""
    
# print multiplication table of n number
"""num = int(input("num:"))
i = 1
while i <= 10:
    print(num*i)
    i += 1"""
    
# print element of the following list using loop [1,4,9,16,25,49,64,81,100]
"""nums = [1,4,9,16,25,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1"""
 
# search number x in this tuple using loop
"""nums = (1,4,9,16,25,49,64,81,100)
x = 25
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at index",i)
    else:
        print("finding")
    i += 1"""
    
    

# Break = used to terminate the loop when encountered
# Continue = terminates execution in the current iteration & continues execution of the
# loop with the next iteration(skip current iteration)

"""nums = (1,4,9,16,25,49,64,81,100)
x = 25
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at index",i)
        break
    else:
        print("finding")
    i += 1
print("end")"""

# odd num
"""i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1"""
    
    

# Loop = used for sequential traversal. for traversing list, string, tuple..
# FOR LOOP

"""nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)

str = "apnacollege"
for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("END")  """


# print element of the following list using FOR loop
"""list = [1, 4, 9,16,25,36,49,64,81,100]
for el in list:
    print(el)"""

# search number X in this tuple using FOR LOOP
"""num = (1, 4, 9,16,25,36,49,64,81,100,49)
x = 49
idx = 0
for el in num:
    if(el == x):
        print("number found at index",idx)
        # break
    idx += 1"""
    
    
    
# range() = range function returns sequence of numbers,starting from 0 by default, and 
# increment by 1(by default), and stops before a specified number..range(start?,stop,step?)
"""for i in range(5):      # range(stop)
   print(i)
for i in range(2,10):   #range(start,stop(not include))
    print(i)
for i in range(1,10,2):   #range(start, stop, step)
    print(i)              # odd number
for i in range(2,101,2):
    print(i)              # even number  """
    

# for & range()..print 1 to 100
"""for i in range(1,101):
    print(i)"""

# 100 to 1
"""for i in range(100,0,-1):
    print(i)"""
    
# multiplication table of number n
"""n = int(input("enter num:"))
for i in range(1, 11):
    print(n*i)"""
    


# pass statement = pass is null statement that does nothing.it is used as a placeholder
#                  for future code
"""for i in range(5):
    pass
if i > 5:
    pass
print("next")    """   



# WAP to find sum of first n natural number(while)
"""n = int(input("enter number:"))
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("sum:",sum)
# for i in range(1,n+1):
#     sum += i
# print("sum:",sum)"""



# find factorial of 1st n number(for)
"""n = 5
fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("fact:",fact)

i = 1
# while i<= n:
#     fact *= i
#     i += 1
# print("fact:",fact)"""


"""list1 = [float, int, "radhe", "mantra", 8, 15, 5, 24, 6]
for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)"""


# Exercise-3  Guess the number
"""n = 8
number_of_guesses = 1
print("you can guess the number only 5 times")
while number_of_guesses <= 5:
    no = int(input("guess the number:\n"))
    if no > n:
        print("plz input small number\n")
    elif no < n:
        print("plz input big number\n")
    else:
        print("win!!\n")
        print(number_of_guesses, "no. of guesses you took to finish!")
        break
    print(5 - number_of_guesses, "guesses left")
    number_of_guesses = number_of_guesses + 1
    if number_of_guesses > 5:
        print("game over")   """
        
        

# Exercise:4  printing pattern
"""print("pattern printing")
num = int(input("enter num of row:"))
bool_var = input("enter 1 or 0:")
if bool_var == "1":
    for i in range(0, num+1):
        print("*"*i)
if bool_var == "0":
    for i in range(num, 0, -1):
        print("*"*i)   """
        
        
# vowels find in string
"""str = input("enter string:")
count = 0
vowels =set ("aeiou")

for char in str:
    if char in vowels:
        count+=1
print(count)  """


# letter frequency
"""word = input("enter word:")
letter = input("enter letter:")
x = word.count(letter)
print(x)
y = int((x/len(word))*100)
print(y)"""