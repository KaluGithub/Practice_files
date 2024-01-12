# Testing Chat GPT Implementation of CSV file grade statistics
# By Mona
# def read_csv(file_path):
# """Reads a CSV file and returns a list of dictionaries."""
data = {}  # data dictionary

file = open("sample_grades.csv") # open a file for reading
for line in file:
    row = line.rstrip().split(",")
    # [0] student, [1] semester, [2] grade
    out = eval(row[1]) #
    if len(row) == 3 and out == Fall 2016:
        if row[2]in data:
            data.count[row[1]] += out
        else:
            data[row[1]] = out
file.close()
for key in data:
    print(key, ":", data[key])  # data [key OR data.get(key)
print()