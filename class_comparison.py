# Comparsion of Fall and Spring Semester grade Statistics
# By Mona
# spring = {}

semester = ["Fall", "Spring"]
data = {}
file = "sample_grades.csv"
# Reading the CSV file
# Loop through all lines in the file
for line in open(file):
    row = line.replace("\n", "")
    row = line.rstrip().split(",")
    # [0] student, [1] semester, [2] grade
    out = eval(row[2]) # NOTE: x NOT a good variable name!
    if len(row) == "fall":
        data[row[1]] += out
    else:
        data[row[1]] = out
file.close()
for key in data:
    print(key, ":", data[key]) # data[key] OR data.get(key)
print()
