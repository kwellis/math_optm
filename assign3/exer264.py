import numpy as np


def func_base(x1, x2):
    return 3 * x1**4 - 2 * x1**3 * x2 - 4 * x1**2 * x2**2 + 5 * x1 * x2**3 + 2 * x2**4


def df_dx1(x1, x2):
    return 12 * x1**3 - 6 * x1**2 * x2 - 8 * x1 * x2**2 + 5 * x2**3


def df_dx2(x1, x2):
    return -2 * x1**3 - 8 * x1**2 * x2 + 15 * x1 * x2**2 + 8 * x2**3


def d2f_dx1_dx1(x1, x2):
    return 36 * x1**2 - 12 * x1 * x2 - 8 * x2**2


def d2f_dx2_dx2(x1, x2):
    return -8 * x1**2 + 30 * x1 * x2 + 24 * x2**2


def d2f_dx1_dx2(x1, x2):
    return -6 * x1**2 - 16 * x1 * x2 + 15 * x2**2


def grad_mat(x1, x2):
    gmat = np.array([df_dx1(x1, x2), df_dx2(x1, x2)])
    return gmat


def hess_mat(x1, x2):
    hmat = np.array([[d2f_dx1_dx1(x1, x2), d2f_dx1_dx2(x1, x2)], [d2f_dx1_dx2(x1, x2), d2f_dx2_dx2(x1, x2)]])
    return hmat


def taylor_approx(x1, x2, p1, p2):
    pmat = np.array([p1, p2])
    fx0 = func_base(x1, x2)
    print(f"Base Function: {fx0}")
    gmat = grad_mat(x1, x2)
    print(gmat)

    hmat = hess_mat(x1, x2)
    print(hmat)
    tapp = fx0 + pmat.T @ gmat + pmat.T @ hmat @ pmat / 2
    return tapp


x1, x2, p1, p2 = 1, -1, 0.1, 0.01
print(f"Assess Point: ({x1+p1}, {x2+p2})")
print(f"True Function Valu is {round(func_base(x1+p1, x2+p2), 3)}")
print(f"Taylor Approximate is {round(taylor_approx(x1, x2, p1, p2), 3)}")
