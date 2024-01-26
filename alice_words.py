# Write a program called alice_words.py
# that creates a text file named alice_words.txt
# containing an alphabetical listing of all the words,
# and the number of times each occurs,
# in the text version of Alice’s Adventures in Wonderland.
# (You can obtain a free plain text version of
# the book, along with many others,
# from http://www.gutenberg.org.)
# The first 10 lines of your
# output file should look something like this:



# Problem Summary: Output key and Values for each word in a file

# First we get Frequency of the words in the file with a dictionary
word_count = {}
dataFile = open("alice_wondld.txt",encoding='utf8')
data = dataFile.read()
lines = data.rstrip().split()

for letter in lines:
     word_count[letter.lower()] = word_count.get(letter, 0) + 1 # lower converts all text to lower case
     letter_items = list(word_count.items())
     letter_items.sort()
out =open("alice_words.txt", "w")
print("Word                       Count", file=out)
print("================================", file=out)
for key in word_count.keys(): # This is using the key method
    print(key, "            ", word_count[key], file=out)


dataFile.close()