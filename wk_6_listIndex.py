# Return The List of files in a Directory of path
# By Mona

import os
for i in os.listdir(): # Empty parameter assumes pwd
    print(i)
print()
# Listing files in a different path

folder_path = "D:\\Bashscripts"
for i in os.listdir(folder_path): # two backslash to avoid escape character issue
    print(i)
print()
# Preceding the path with r designates it as a raw string
for i in os.listdir(r"C:\Users\monau\PycharmProjects\Joy_of_Coding\Practice_files"):
    print(i)
