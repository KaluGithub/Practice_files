# Writing Files Practice
# Writing Files Practice
# By Mona

# Q 1. Write a python program that reads in a text file and prints all the lines back out with a
# dash in front.


# dataFile = open("add.txt")
# for line in dataFile:
#     print("-", line.rstrip())
################################################
# Reading & Updating Text files for W3

# dataFile  = open("text2.txt", "a")
# dataFile.write("Did we create a new file? Now the file has more content!")
# ##########################################################
# dataFile = open("text2.txt", "r")
# print(dataFile.read())
###########################################################
# Reading text files from my laptop Practice

# dataFile = open("welcome.txt", "r")
# lines = len(dataFile.readlines())
# print("Total Number of lines:", lines)

#########################################################################
# Counting number of words in my file
# creating variable to store the
# number of words
number_of_words = 0

# Opening our text file in read only
# mode using the open() function
with open(r'welcome.txt','r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Splitting the data into separate lines
	# using the split() function
	lines = data.split()

	# Adding the length of the
	# lines in our number_of_words
	# variable
	number_of_words += len(lines)


# Printing total number of words
# print(number_of_words)
#
# count = 0
# dataFile = open("welcome.txt")
# data = dataFile.read()
# lines = data.split()
# count += len(data)
# # for d in data:
# print(count)

# Print Dictionary

# dataFile.close()