#Write a program that reads a string and returns a
# table of the letters of the alphabet in alphabetical order
# which occur in the string together with the number of times
# each letter occurs. Case should be ignored.
# A sample output of the program when the user enters the data
# “ThiS is String with Upper and lower case Letters”, would look this this:

# By Mona
# For key and Values in a word
letter_count = {}
for letter in "Mississippi":
    letter_count[letter] = letter_count.get(letter, 0) + 1
for key in letter_count.keys(): # This is using the key method
    print(key, letter_count[key])

# Output key and Values for each word in a file

# First we get Frequency of the words in the file with a dictionary
word_count = {}
dataFile = open("turing.txt")
data = dataFile.read()
lines = data.split()
for letter in lines:
     word_count[letter] = word_count.get(letter, 0) + 1

for key in word_count.keys(): # This is using the key method
    print("The number of times,", key, "appeared in this file is ;", word_count[key])



dataFile.close()
