# Program that takes users input and writes to file
# By Mona

# 2. Write a python program that asks the user for the name of a file, and then repeatedly
# asks the user to enter a number, entering the number ‘0’ when finished. Output each of
# these numbers to the file on a separate line.

# Enter data into the file for i in range(10): f.write("This is line %d\r\n" % (i+1))
PROMPT = "Enter a number or Enter 0 to exit: "
outfilename = input("What is the name of your output file? ")
# Create a new file object, in "write mode
dataFile = open(outfilename, "w") # a to append
userinput = eval(input(PROMPT))
while userinput != 0:
    print(userinput, file=dataFile)
    userinput = eval(input(PROMPT))

# close the file with the method "close"
dataFile.close()
