# Predict ME!
# What do you think is output by this program?

data = {}  # data dictionary

file = open("sample_grades.csv") # open a file for reading
for line in file:
    row = line.rstrip().split(",")
    # [0] student, [1] semester, [2] grade
    out = eval(row[2]) #
    if len(row) == 3 and out == 100:
        if row[1]in data:
            data[row[1]] += out
        else:
            data[row[1]] = out
file.close()
for key in data:
    print(key, ":", data[key])  # data [key OR data.get(key)
print()