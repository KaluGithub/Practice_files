# Function count_unique that takes a string
# of sorted numbers as a parameter and returns
# the number of unique numbers  using a dictionary

# Dictionaries walk through

def count_unique(str):
    d_unique = {}  # Create new dictionary
    for a in str:
        if a not in d_unique:
            d_unique[a] = 1 # Could be anything
    return len(d_unique)    # number of keys

def main():
    print(count_unique("111224446"))== 4
    print(count_unique("304447755555"))== 5
    print(count_unique(""))== 0


main()