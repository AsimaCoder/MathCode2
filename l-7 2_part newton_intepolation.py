import numpy as np

def interpolate_newton_forward(x_points, y_values, target_value):
    # Determine the number of points
    points_count = len(x_points)
    # Assume uniform spacing between x points
    interval = x_points[1] - x_points[0]

    # Build the forward difference table
    forward_diff_table = [y_values.copy()]
    for level in range(1, points_count):
        level_diffs = []
        for i in range(points_count - level):
            diff = forward_diff_table[level - 1][i + 1] - forward_diff_table[level - 1][i]
            level_diffs.append(diff)
        forward_diff_table.append(level_diffs)

    # Identify the correct interval for the target x value
    interval_index = np.searchsorted(x_points, target_value) - 1

    # Calculate the interpolation value using Newton's forward formula
    s = (target_value - x_points[interval_index]) / interval
    interpolated_value = y_values[interval_index]
    for level in range(1, points_count - interval_index):
        product_term = np.prod([(s - k) for k in range(level)]) / np.math.factorial(level)
        interpolated_value += product_term * forward_diff_table[level][interval_index]

    return interpolated_value

# Input data
x_data = [1, 1.4, 1.8, 2.2]
y_data = [3.49, 4.82, 5.96, 6.5]

# Target x for interpolation
target_x_value = 1.6

# Perform interpolation
interpolated_value = interpolate_newton_forward(x_data, y_data, target_x_value)

print(f"Interpolated value at x = {target_x_value}: {interpolated_value:.4f}")
