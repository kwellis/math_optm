import numpy as np


def six_exp(x1, x2):
    return np.exp(-(x1**2) - 2 * x1 + 3 * x2 - x2**2)


def six_hessian(x1, x2):

    df2_dx1_dx1 = 4 * x1**2 + 8 * x1 + 2
    df2_dx2_dx2 = 4 * x2**2 - 12 * x2 + 7
    df2_dx1_dx2 = 4 * x1 * x2 - 6 * x1 + 4 * x2 - 6

    hess = np.matrix([[df2_dx1_dx1, df2_dx1_dx2], [df2_dx1_dx2, df2_dx2_dx2]])

    # hess = six_exp(x1, x2) * hess  # properly distribute the expoential, can this math be done without worrying?

    return hess


new_hess = six_hessian(-1, 3 / 2)
print("\nExponential Value:")
print(six_exp(-1, 3 / 2))

print("\nHessian Matrix")
print(six_hessian(-1, 3 / 2))

print("\nDeterminant")
print(np.linalg.det(new_hess))

print("\nEigenValues:")
print(np.linalg.eigvals(new_hess))

"""Apparently:

If you have two negative eigenvalues, the point is a local maximum. Or if the determinant
of the matrix is non-negative at the location and the h11 point is negative, that is also
a method for knowing that you have a local maximum?
"""
