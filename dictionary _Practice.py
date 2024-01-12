# Practice Dictionary
# By Mona

# Dictionary from ascii
# Key: Value pairs

# Dictionary Operations

# Indexing <dict>[<key>]
empty_dic = {}
ascii = {"a": 97, "b": 98, "c": 99}

contacts = {"James" : 800, "John": 900, "Peter": 700}

print(ascii.keys())   # Indexing
print()
print(len(ascii))       # Length (# of keys)
print()
for a in ascii:         # Iteration
    print(ascii.values())
    print()
print("a" in ascii)    # Membership
print()
print(ascii["c"])   # Accessing Values using keys; key error if key is not in dictionary
print()
print(ascii.get("b")) # Accessing values using get method
print()

print(contacts.get("John"))
print()
print(contacts.get("Luke"))     # If no mapping, None is returned instead of keyError
print()

if "Luke" in contacts:
    number = contacts["Luke"]   # Know mapping exists before trying to access
else:
    print("Not in Contact")
    print()

ascii["d"] = 87   # Inserting  Key-Value Pairs
print(ascii)
print()
ascii["e"], ascii["f"], ascii["h"] = 90, 81, 79  # Inserting Multiple key-values pairs
print(ascii)
print()

contacts["John"] = 1000    # Adding/ Modifying Key-Value Pairs
print(contacts)
print()

contacts["Katy"] = 3000    # Adding/ Modifying Key-Value Pairs
print(contacts)
print()

# Methods key() and Values ()
# To make a dictionary into a list:
# keys = list(mydict.keys())

tel_numbers = list(contacts.values())
print(tel_numbers)
print()