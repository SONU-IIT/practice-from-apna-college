import numpy as np

A = np.array([15, 25, 35])
B = np.array([10, 20, 30])
C = A + B
#print("Resulting vector C:", C)

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
#print("v1 + v2:", v1 + v2)

v1 = np.array([1, 2, 3])
v2 = np.array([[4], [5], [6]])
#print("v1 + v2 with broadcasting:", v1 + v2)

v1 = np.array([1, 2, 3])
v2 = np.array([[4], [5], [6]])
#print("v1 * v2:", v1 * v2)

import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
A_T = A.T
#print(A_T)

A = np.array([[1,2,3]])
value = np.linalg.norm(A)
#print(A)
#print(A.T)


#BDA SESSION
