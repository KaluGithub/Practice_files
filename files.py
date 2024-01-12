# Practice with files and dictionaries
# Count the number of lines in a file
# Using a dictionary

# By Mona Kalu

letters = ["A", "B", "C", "D", "E", "F"]
file = "letters.txt"
counts = {}

# loops through all lines in the file
for line in open(file):
    # To remove extra space in txt file; If commas, use split
    letter = line.replace("\n", "")
    # print(letter) # Testing
    # get the count of line/letter if it exist, 0 otherwise
    count = counts.get(letter, 0)
    counts[letter] = count + 1
for l in letter:
    print("Letters Counts:")
    print(l + ":", counts.get(l, 0))
# for items in counts.keys():
#     print(item + "+", count[item])
