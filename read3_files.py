# Program to read from 3 different text files
# By Mona

# 3. Write a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts
# the number of lines in each file, and prints out the number of lines to a file counts.txt.

def count_lines(filename):
    total = 0
    for line in open(filename):
        total +=1
    return filename + ":" + str(total)

    list = ["test1_txt", "test2.txt", "test3.txt"]
    out =open("counts.txt", "w")
    for file in list:
        print(count_lines(file), file=out)

file = open("test1.txt", "r")
Counter = 0
# Reading from file
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
# Print number of lines
print("Test1.txt: ", Counter)
counter = 0
def count_line(filename):
    with open("filename", "r") as file:
        # counter = 0
# Reading from file
        content = file.read()
        coList = content.split("\n")
        for i in coList:
            if i:
                counter += 1
            return counter
# Print number of lines
            print("filename: ", counter)

file.close()

def count_lines(filename):
    total = 0
    for line in open(filename):
        total += 1
    return filename + " : " + str(total)

list = ["test1.txt", "test2.txt", "test3.txt"]
out = open("counts.txt", "w")
for file in list:
    print(count_lines(file), file=out)


out.close()
