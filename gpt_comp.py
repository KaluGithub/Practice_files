# Using Chat GPT for Class grade comparison
# By Mona
# Reading CSV file
# Open the file in read mode

def read_csv(file_path):
    """Reads a CSV file without a header and returns a list of dictionaries."""
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            data.append({'Name': values[0], 'Semester': values[1], 'Grades': values[2]})
    return data


def calculate_mean(data):
    """Calculates the mean of a list of numbers."""
    return sum(data) / len(data) if len(data) > 0 else 0


def calculate_median(data):
    """Calculates the median of a list of numbers."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def calculate_std_dev(data, mean):
    """Calculates the standard deviation of a list of numbers."""
    n = len(data)
    if n == 0:
        return 0
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / n
    return variance ** 0.5


def calculate_stats(data):
    """Calculates mean, median, and standard deviation for fall and spring grades."""
    fall_grades = [float(row['Grades']) for row in data if row['Semester'] == 'Fall']
    spring_grades = [float(row['Grades']) for row in data if row['Semester'] == 'Spring']

    fall_mean = calculate_mean(fall_grades)
    spring_mean = calculate_mean(spring_grades)

    fall_median = calculate_median(fall_grades)
    spring_median = calculate_median(spring_grades)

    fall_std = calculate_std_dev(fall_grades, fall_mean)
    spring_std = calculate_std_dev(spring_grades, spring_mean)

    return {
        'Fall': {'Mean': fall_mean, 'Median': fall_median, 'Std Dev': fall_std},
        'Spring': {'Mean': spring_mean, 'Median': spring_median, 'Std Dev': spring_std}
    }


if __name__ == "__main__":
    # Replace 'your_file.csv' with the actual file path
    file_path = 'sample_grades.csv'

    # Read CSV file
    data = read_csv(file_path)

    # Calculate and print statistics
    stats = calculate_stats(data)

    print("Statistics for Fall Semester:")
    print(f"Mean: {stats['Fall']['Mean']}")
    print(f"Median: {stats['Fall']['Median']}")
    print(f"Standard Deviation: {stats['Fall']['Std Dev']}\n")

    print("Statistics for Spring Semester:")
    print(f"Mean: {stats['Spring']['Mean']}")
    print(f"Median: {stats['Spring']['Median']}")
    print(f"Standard Deviation: {stats['Spring']['Std Dev']}")
