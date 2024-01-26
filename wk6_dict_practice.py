# This problem is to form a frequency table
# of the letters in the string, that is,
# how many times each letter appears.
# https://carrot.whitman.edu/Thinkcspy/dictionaries.html

# Mona

# letter_count = {}
# for letter in "Mississippi":
#      letter_count[letter] = letter_count.get(letter, 0) + 1
# print(letter_count)

word_count = {}
dataFile = open("turing.txt")
data = dataFile.read()
lines = data.split()
for letter in lines:
     word_count[letter] = word_count.get(letter, 0) + 1
print(lines)
print(word_count)


dataFile.close()

