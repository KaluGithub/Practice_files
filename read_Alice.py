# Reading the text file of Alice in wonderland before processing
# By Mona

# dataFile = open("alice_wondld.txt")
# data = dataFile.read()
# lines = data.rsplit()
# print(lines)


# letters = ["A", "B", "C", "D", "E", "F"]
file = "alice_wondld.txt"
counts = {}

# loops through all lines in the file
for line in open(file):
    # To remove extra space in txt file; If commas, use split
    letter = line.replace("\n", "")
    print(letter) # Testing
#     # get the count of line/letter if it exist, 0 otherwise
#     count = counts.get(letter, 0)
#     counts[letter] = count + 1
# for l in letter:
#     print("Letters Counts:")
#     print(l + ":", counts.get(l, 0))