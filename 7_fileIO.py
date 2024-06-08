# File I/O = python can be used to perform operation on a file(read & write data)
# text file(character) = .txt, .docx, .log
# binary file = .mp4, .mov, .png, .jpeg

# Open, Read & Close File = we have to open file before read or write
# f = open("file_name","mode")

"""f = open("7_file.txt","r")
data = f.read()        # reads entire file
print(data)
print(type(data))

line1 = f.readline()   # reads one line at a time
print(line1)
f.close()"""


# Writing to file
"""f = open("7_file.txt","w")        # overWrite the entire file
f.write("i want to learn js")
f.close()"""

"""f = open("7_file.txt", "a")       # append at the end to the file
f.write("\nthen i will move to js")
f.close()"""


"""f = open("7_file.txt", "r+")        # replace the text from starting (no truncate)
f.write("abcd")                        # read & over write (pointer at the start)
print(f.read())   # pointer moves to the replace text so it reads from old text
f.close()"""


"""f = open("7_file.txt", "w+")   # it will erase all data from file & then we can add new data
f.close()"""                      # read & overwrite (truncate = erase all data)

"""f = open("7_file.txt", "a+")   # read & append(pointer at the end)
f.write("ishita")                 # no truncate
f.close()"""


# with syntax
"""with open("7_file.txt", "r") as f:
    data = f.read()
    print(data)  """       # automatically close the file in with syntax
    

# deleting a file = using the os module
# Module(like a code library) is a file written by another programmer that generally has
# a function we can use
"""import os 
os.remove("sample.txt")"""



# create new file "practice.txt" using py. add following data
with open("practice.txt","w") as f:
    f.write("Hi,everyone\nwe are learning file I/o\n")
    f.write("using Java\nI like programming in Java")


# replace all occurrence of "Java" to "Python" in above file
"""with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)"""
    
    
# search if the word "learning" exist in file or not (by function)
"""def check_word():
    with open("practice.txt","r") as f:
        data = f.read()
        word = "learning"
        if(data in word):
            print("found")
        else:
            print("not found")
check_word()"""


# find in which line of the file does the word "learning" occur first..print-1 if word not found
"""def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_line()"""


# from a file containing numbers separated by comma,print the count of even numbers
"""count = 0
with open("practice.txt", "w") as f:
    data = f.read()
        
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
print(count)
    """