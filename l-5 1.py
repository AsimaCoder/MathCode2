import numpy as np

def invert_matrix_cayley_hamilton(matrix):
    size = matrix.shape[0]
    identity = np.eye(size)
    inverse = np.zeros_like(matrix, dtype=float)
    char_poly_coeffs = np.poly(matrix)[::-1]  # Characteristic polynomial coefficients

    matrix_power = identity.copy()
    for i, coeff in enumerate(char_poly_coeffs[:-1]):
        inverse += coeff * matrix_power
        if i < size - 1:
            matrix_power = np.dot(matrix, matrix_power)
    
    inverse /= -char_poly_coeffs[-1]  # Normalize by last coefficient

    return inverse

# Test matrix
A = np.array([[1, 1, 2], [0, -2, 0], [0, 0, 3]])
A_inv = invert_matrix_cayley_hamilton(A)

print("Inverse of A:")
print(A_inv)
