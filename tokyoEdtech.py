# Strings, List  Dictionary
# By Mona

# file = open
# Create 2 list with fall and spring grades
import statistics

fall = []
spring = []

# Defining Statistics for grades

def grade_stats(list):
    print("Mean:    ", statistics.mean(list))
    print("Median:  ", statistics.median(list))
    print("STD:     ", statistics.stdev(list))
    print()

# Load data into string variable
# def read_csv(filepath)
with open("sample_grades.csv", "r") as file:
    # Create a list of each row
    for line in file:
        list = line.rstrip().split(",")
        # Check if row is the proper length
        if len(list) == 3:
            # Separate out the data
            name = list[0]
            semester = list[1]
            grade = list[2]
            # define and populate List
            # with fall & Spring Grades
            if list[1] == "Spring 2016":
                spring.append(eval(list[2])) # use eval to change string 'Grade' to integer and append it to empty list
            else:
                fall.append(eval(list[2]))
file.close()

print("Fall Grades: ",   fall)
print("Spring Grades: ", spring)

print("Spring Mean: ", statistics.mean(spring))



















###################################################
# fall_Gcount = 0
# # file = open
# # Create 2 dictionaries for fall and spring grades
# fall_grades = {}
# spring_grades = {}
# # Load data into string variable
# with open("sample_grades.csv", "r") as file:
#     # Create a list of each row
#     for line in file:
#         data = line.rstrip().split(",")
#         # Check if row is the proper length
#         if len(data) == 3:
#             # Separate out the data
#             name = data[0]
#             semester = data[1]
#             grade = data[2]
#             letters = ["Fall 2016", "Spring 2016"]
#             # print(f"Name: {name}, Semester: {semester}, Grade: {grade}")
#             # Populate Dictionary
#             # Count number of fall & Spring Grades
#
#             for d in data:
#                 if semester == "Fall 2016":
#                     fall_grades[semester] = eval(grade)
#                     fall_Gcount += 1
#                 else:
#                     spring_grades[semester] = eval(grade)
#     print(fall_grades, spring_grades)
