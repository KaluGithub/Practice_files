# Problem
# Count_unique(string) Write a function count_unique that takes a string of sorted numbers
# as parameter and returns the number of unique numbers using a dictionary.


def count_unique(str):
    d = {}  # Create a Dictionary
    for letter in str:
        if letter not in d:
            d[letter] = 1 # could be anything
    return len(d)  # Number of keys


