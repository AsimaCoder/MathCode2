import numpy as np

# Input data
x_points = np.array([1, 2, 3, 4, 5])
y_points = np.array([14, 27, 40, 55, 68])

# Calculate necessary summations for linear regression equations
total_x = np.sum(x_points)
total_y = np.sum(y_points)
total_x_squared = np.sum(x_points ** 2)
total_xy = np.sum(x_points * y_points)
data_count = len(x_points)

# Construct matrices for linear equations
matrix_left_side = np.array([[total_x_squared, total_x],
                             [total_x, data_count]])
matrix_right_side = np.array([total_xy, total_y])

# Solve linear equations to find slope (m) and intercept (c)
slope, intercept = np.linalg.solve(matrix_left_side, matrix_right_side)

# Output the linear equation in a readable format
print(f"Linear equation: y = {slope:.2f}x + {intercept:.2f}")
