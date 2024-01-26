# Activity Array & Files : Week 6
# Program to store each line of file as a separate element in a file.
# By Mona

file = open("turing.txt")
lines = []
for line in file:
    lines.append(line.rstrip())

file.close()
# print(lines[:2])
# print(lines[-2:])
# think of ways to make this code DRYer
