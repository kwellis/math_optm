import numpy as np


def func_base(x1, x2):
    """Euclidean Norm"""
    return np.sqrt(x1**2 + x2**2)


def df_dx1(x1, x2):
    return x1 * (x1**2 + x2**2) ** (-1 / 2)


def df_dx2(x1, x2):
    return x2 * (x1**2 + x2**2) ** (-1 / 2)


def d2f_dx1_dx1(x1, x2):
    return x2**2 * (x1**2 + x2**2) ** (-3 / 2)


def d2f_dx2_dx2(x1, x2):
    return x1**2 * (x1**2 + x2**2) ** (-3 / 2)


def d2f_dx1_dx2(x1, x2):
    return -x1 * x2 * (x1**2 + x2**2) ** (-3 / 2)


def grad_mat(x1, x2):
    gmat = np.array([df_dx1(x1, x2), df_dx2(x1, x2)])
    return gmat


def hess_mat(x1, x2):
    hmat = np.array([[d2f_dx1_dx1(x1, x2), d2f_dx1_dx2(x1, x2)], [d2f_dx1_dx2(x1, x2), d2f_dx2_dx2(x1, x2)]])
    return hmat


x1, x2 = 3, 4
print(f"Term One: {func_base(x1, x2)}")
print(f"Gradient Matrix: {grad_mat(x1, x2)}")
print(f"Hessian Matrix:\n {hess_mat(x1, x2)}")
