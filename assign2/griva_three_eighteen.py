import numpy as np

big_X = np.matrix([[0, 1, 3], [0, 4, 1], [1, 1, 1]])
lil_y = np.array([2, 2, 1])

alpha = np.matmul(np.linalg.inv(big_X), lil_y)

a1, a2, a3 = alpha[0, 0], alpha[0, 1], alpha[0, 2]


def func(x1, x2, x3, a1, a2, a3):
    return a1 * x1 + a2 * x2 + a3 * x3


print(a1, a2, a3)

print(func(0, 1, 3, a1, a2, a3))
print(func(0, 4, 1, a1, a2, a3))

# the key is that all the coefficients have to sum up to equal one
# also, I really don't understand why we need these convex combinations?
# what good are they? Just a simplification of the points, and math?
