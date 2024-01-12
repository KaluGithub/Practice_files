# Pylenin

counts = 0
file = open("sample_grades.csv")
for line in file:
    row = line.rstrip().split(",")
    print(row)

