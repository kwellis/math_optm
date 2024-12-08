# attempt these by hand to ensure you understand what you are doing...

import numpy as np

print("Part I:")
a_mat = np.array([[1, 1, 1, 1], [1, -1, -1, 1], [0, 1, 0, 1]])

b_idx = [0, 1, 2]  # define the 1st, 2nd and 3rd row indexs
n_idx = [3]

b_mat = a_mat[:, b_idx]
n_mat = a_mat[:, n_idx].reshape(-1, 1)  # might need rewrite how the shaping is occuring

b_inv = np.linalg.inv(b_mat)
top = np.dot(-1 * b_inv, n_mat)

Z = np.vstack((top, np.eye(1)))
print(f"The Null Basis is:\n {Z}")  # this is actually showing the null matrix?
print(f"Confirm AZ is zero:\n {a_mat @ Z}")
print(f"Rank of Z is {np.linalg.matrix_rank(Z)}")

print("\nPart II:")
a_mat = np.array([[1, 1, 1, 1]])

b_idx = [0]  # define the 1st, 2nd and 3rd row indexs
n_idx = [1, 2, 3]

b_mat = a_mat[:, b_idx]
n_mat = a_mat[:, n_idx]  # have to reshape uptop, not down here...?

b_inv = np.linalg.inv(b_mat)
b_inv = float(b_inv[0, 0])
top = np.dot(-1 * b_inv, n_mat)

Z = np.vstack((top, np.eye(len(n_idx))))
print(f"The Null Basis is:\n {Z}")
print(f"Confirm AZ is zero:\n {a_mat @ Z}")
print(f"Rank of Z is {np.linalg.matrix_rank(Z)}")

print("\nPart III")
a_mat = np.array([[1, 1, 1, 1], [1, -1, -1, 1]])

b_idx = [0, 1]  # define the 1st, 2nd and 3rd row indexs
n_idx = [2, 3]

b_mat = a_mat[:, b_idx]
n_mat = a_mat[:, n_idx]

b_inv = np.linalg.inv(b_mat)
top = np.dot(-1 * b_inv, n_mat)

Z = np.vstack((top, np.eye(len(n_idx))))
print(f"The Null Basis is:\n {Z}")
print(f"Confirm AZ is zero:\n {a_mat @ Z}")
print(f"Rank of Z is {np.linalg.matrix_rank(Z)}")

print("\nPart IV")
a_mat = np.array([[1, 1, 1, 1], [2, 0, 0, 2], [1, -1, -1, 1]])

# starting with variable reduction, which doesn't work
b_idx = [0, 1, 2]  # define the 1st, 2nd and 3rd row indexs
b_mat = a_mat[:, b_idx]
print(f"The Determinent of the Basic Matrix is: {np.linalg.det(b_mat)}")
# since the determinant is 0 the matrix is non-invertable...

# using QR factorization
Q, R = np.linalg.qr(a_mat.T, mode="complete")  # need transpose and complete mode...

print(f"The Q Matrix:\n{Q}\nThe R Matrix:\n{R}")

m, n = a_mat.shape
r = np.linalg.matrix_rank(a_mat)  # matrix rank
q2_col = n - r  # not sure why you don't need to correct for python index...? Complete mode?
Q2 = Q[:, q2_col:]
Z = Q2

print(f"The Null Basis is:\n {Z}")
print(f"Confirm AZ is zero:\n {np.allclose(a_mat @ Z, np.zeros_like(a_mat @ Z))}")
print(f"Rank of Z is {np.linalg.matrix_rank(Z)}")
