import numpy as np

def find_dominant_eigenpair(matrix, iterations=1000):
    dimension = matrix.shape[0]
    vec = np.random.rand(dimension, 1)  # Starting with a random vector

    for _ in range(iterations):
        vec_next = matrix @ vec  # Matrix-vector multiplication
        vec_next_norm = np.linalg.norm(vec_next)
        vec = vec_next / vec_next_norm  # Normalizing vector

    # Calculate the corresponding eigenvalue
    dominant_eigenvalue = (vec.T @ matrix @ vec).item()

    return dominant_eigenvalue, vec.ravel()

# Example matrix
matrix_example = np.array([[1, 2], [3, 4]])

# Compute the dominant eigenvalue and eigenvector
dominant_eigenvalue, dominant_eigenvector = find_dominant_eigenpair(matrix_example)

print("Dominant eigenvalue:", dominant_eigenvalue)
print("Dominant eigenvector:", dominant_eigenvector)
