# Input data points
x_points = [10, 20, 30, 40]
y_points = [1.1, 2.0, 4.4, 7.9]

# Initialize the forward difference table using the initial y values
difference_table = [y_points]

# Iteratively compute forward differences
for level in range(1, len(x_points)):
    current_differences = []
    for index in range(1, len(difference_table[level - 1])):
        # Calculate the difference at the current level
        diff = difference_table[level - 1][index] - difference_table[level - 1][index - 1]
        current_differences.append(diff)
    # Append the current level differences to the table
    difference_table.append(current_differences)

# Display the forward difference table
print("Forward Difference Table:")
for level, differences in enumerate(difference_table):
    print(f"Δ^{level}y:", differences)
