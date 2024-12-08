import numpy as np

print("Part I")
a_mat = np.array([[1, 2, 0, 2], [2, 1, 2, 4]])

b_idx = [1, 2]  # define the 1st, 2nd and 3rd row indexs
n_idx = [0, 3]

b_mat = a_mat[:, b_idx]
n_mat = a_mat[:, n_idx]

b_inv = -1 * np.linalg.inv(b_mat)
top = np.dot(b_inv, n_mat)

basis = np.vstack((top, np.eye(len(n_idx))))
print(basis)  # this is actually showing the null matrix?

# need to think about a function to automatically generate this new order
# use the b_idx and n_idx order as the inputs, create how to reorder stuff
new_order = [
    2,  # the old 2 becomes 0
    0,  # the old 0 becomes 1
    1,  # the old 1 becomes 2
    3,  # the old 3 stays a 3
]
basis_order = basis[new_order, :]
print(basis_order)

# print(a_mat @ basis_order)

print("Part II")
"""Can't use p1 and p4 as the basic variables because they are linear multiples of each other...
Basically if you multiple p1 times 2 you get p4. As a result the determinent of there matrix is
going to be zero, so you don't have a determinent. Maybe it would work for QR factorization???"""
