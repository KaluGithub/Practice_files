# Using File I/O ppt for review and practice
# By Mona

# Definition: A file is a Sequence of data stored in Memory
# To use a file, create an object of type file

# file is a data type
# <varname>:string
# <mode>: string, "r" for read, "w" for write, "a" for append(etc)

# Exp: dataFile = open("years.dat", "r")

# Common File Methods
# read(): Read the entire content from the file, returned as a string object


myFile = "test3.txt"
for line in open(myFile): # For each line in the file, do something
    letter = line.replace("\n", "")
    # line = line.replace("\n", "")
    # letter = line.rstrip()
    print(letter)
    print()


# Creating a txt file from user input

FILENAME = "test1.txt"
dataFile = open("test1.txt", "r")
line = dataFile.readline()
while line != "":
    line = line.rstrip()
    print(line)
    line = dataFile.readline()

dataFile.close()







