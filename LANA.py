import numpy as np
matrix = np.array([[1, 2],[3, 4]])
print(matrix)

#finding determinant of matrix
determinant = int(np.linalg.det(matrix))
print("Determinant of the matrix is:", determinant)

#finding inverse of matrix2
matrix2 = np.array([[1, 2], [3, 4]])
print("Inverse of matrix2 is:", np.linalg.inv(matrix2))