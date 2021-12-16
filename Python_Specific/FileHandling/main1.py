# Note
# rstrip(): This function strips each line of a file off spaces from the right-hand side.
# lstrip(): This function strips each line of a file off spaces from the left-hand side.

"""
 f = open(filename, mode)
 r: open an existing file for a read operation.
 w: open an existing file for a write operation. If the file already contains some data then it will be overridden. 
 a:  open an existing file for append operation. It won’t override existing data.
 r+:  To read and write data into the file. The previous data in the file will not be deleted.
 w+: To write and read data. It will override existing data.
 a+: To append and read data from the file. It won’t override existing data.
"""

# Ways TO Open File
file = open("./FileHandling/test.txt", 'r')

for each in file:
    print(each.strip())

file.close()

# Another way
with open("file.txt") as file:
    data = file.read()

# split() using file handling
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

"""
seek() method
In Python, seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file. 
"""
# Syntax = file.seek(number)

# prints current position
print(f.tell())
