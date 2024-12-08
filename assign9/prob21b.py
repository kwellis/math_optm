import numpy as np
from scipy.linalg import null_space
from scipy.optimize import fsolve


def lagrange_values(x1, x2):
    """Find the Values for Lambda 1 and 2 that calculate
    where the gradient is equal to zero for defined values
    of x.
    """
    A = np.array([[2 * x1, 0], [2 * x2, -1]])
    b = np.array([2 - 2 * x1, -2 - 2 * x2])
    l1, l2 = np.linalg.inv(A) @ b
    return l1, l2


def grad_one(x1, l1):
    return 2 * x1 + 2 * l1 * x1 - 2


def grad_two(x2, l1, l2):
    return 2 * x2 + 2 * l1 * x2 - l2 + 2


def null_jac_one(x1, x2):
    jac = np.array([[2 * x1], [2 * x2]])
    print(jac)
    z = null_space(jac)
    return z


def null_jac_two(x1, x2):
    jac = np.array([[0], [1]])
    print(jac)
    z = null_space(jac)
    return z


print(null_jac_two(0, 0))
