# Data Project Practice
# by Mona Kalu

import statistics
def output_Stats(list):
    print("Mean: ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD: ", statistics.stdev(list))
    print()
# Data Variables
spring = []
fall = []

# Read in the File
def read_csv(filepath):
    file = open(filepath.csv)
    for line in file:
        list = line.rstrip().split(",")
        # print(list)
        if list[1] == "Spring 2016":
            spring.append(eval(list[2]))
        else:
            fall.append(eval(list[2]))


# file.close()
def main():
    # print(read_csv("sample_grades.csv)", "spring"))
    # print(read_csv("sample_grades.csv)", "fall"))
    print("Fall 2016: ")
    output_Stats(fall)
    print("Spring 2016: ")
    output_Stats(spring)



main()


