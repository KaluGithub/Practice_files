# Wk 6 Dictionary Practice:
# To display the frequency table in alphabetical order.
# We can do that with the items and sort methods:
# By Mona

letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)

# Frequency of words in a file

word_count = {}
dataFile = open("turing.txt")
data = dataFile.read()
lines = data.split()
for letter in lines:
     word_count[letter] = word_count.get(letter, 0) + 1
#Notice in the first line we had to call
# the type conversion function list.
# That turns the promise we get from items into a list,
# a step that is needed before we can use the list’s sort method.
word_items = list(word_count.items())
word_items.sort()
print(word_items)

print(lines)
print(word_count)


dataFile.close()