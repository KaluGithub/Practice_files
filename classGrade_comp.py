# Strings, List  Dictionary
# By Mona

# file = open
# Create 2 dictionaries for fall and spring grades
counts = {}
# Load data into string variable
with open("sample_grades.csv", "r") as file:
    # Create a list of each row
    for line in file:
        data = line.rstrip().split(",")
        # Check if row is the proper length
        if len(data) == 3:
            # Separate out the data
            name = data[0]
            semester = data[1]
            grade = eval(data[2])
            letter = ["Fall 2016", "Spring 2016"]
            # print(f"Name: {name}, Semester: {semester}, Grade: {grade}")
            # Populate Dictionary
            # Count number of fall & Spring Grades
            count = counts.get(letter, 0) # gets the count of fall and spring grades or 0 no letter
            counts[letter] = count  # Store count
            # print out counts
        for l in letter



    print()