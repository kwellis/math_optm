import numpy as np


def func(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> np.ndarray:
    return 1 / 2 * x.T @ Q @ x - c.T @ x


def grad(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> np.ndarray:
    return Q @ x - c


def yk_quasi(xkpo: np.ndarray, xk: np.ndarray, Q: np.ndarray, c: np.ndarray) -> np.ndarray:
    """yk, Difference Between Two Gradients

    Args:
        xkpo (np.ndarray): Array of x_k+1 values
        xk (np.ndarray): Array of x_k values
        Q (np.ndarray): Quadratic Matrix
        c (np.ndarray): C vector
    """
    return grad(xkpo, Q, c) - grad(xk, Q, c)


def sk_quasi(xkpo: np.ndarray, xk: np.ndarray) -> np.ndarray:
    """sk, Difference Between Two Vectors

    Args:
        xk (np.ndarray): Array of x_k values
        xkmo (np.ndarray): Array of x_k-1 values
    """
    return xkpo - xk


def pk_quasi(Bk: np.ndarray, dfk: np.ndarray) -> np.ndarray:
    """Search Direction

    How is this more efficient than finding inverse of Hessian...?

    Args:
        Bk (np.ndarray): Quasi Hessian at xk
        dfk (np.ndarray): Gradient at xk
    """
    return -np.linalg.inv(Bk) @ dfk  # does Bk need to be transposed?


def Bk_quasi(Bk: np.ndarray, yk: np.ndarray, sk: np.ndarray) -> np.ndarray:
    para = yk - Bk @ sk
    ftop = np.outer(para, para)  # ftop = para @ para.T
    fbtm = para.T @ sk
    bk_add = ftop / fbtm
    return Bk + bk_add


def alpha_quad(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> float:
    # is the book using a different line search method?
    a_top = -grad(x, Q, c).T @ grad(x, Q, c)
    a_btm = -grad(x, Q, c).T @ Q @ -grad(x, Q, c)
    return float(-a_top / a_btm)


def alpha_book(pk: np.ndarray, dfk: np.ndarray, Q: np.ndarray) -> float:
    # the book uses a different line search method?
    a_top = pk.T @ dfk
    a_btm = pk.T @ Q @ pk
    return float(-a_top / a_btm)


def quasi_newt_rank_one(
    x0: np.ndarray, B0: np.ndarray, Q: np.ndarray, c: np.ndarray, tol: float = 1e-8, max_iter: int = 250
) -> tuple[np.ndarray, int]:
    xk = x0
    Bk = B0
    k = 0
    while np.linalg.norm(grad(xk, Q, c)) > tol:
        pk = pk_quasi(Bk, grad(xk, Q, c))  # search direction
        dfk = grad(xk, Q, c)  # gradient
        ak = alpha_book(pk, dfk, Q)
        if k == max_iter:
            break
        k += 1
        xkpo = xk + ak * pk  # x_k+1
        sk = sk_quasi(xkpo, xk)
        yk = yk_quasi(xkpo, xk, Q, c)
        Bk = Bk_quasi(Bk, yk, sk)
        xk = xkpo
    return xk, k


print("Exercise 12.3.1")
Q = np.array([[5, 2, 1], [2, 7, 3], [1, 3, 9]])
c = np.array([-9, -0, -8])
x_star = np.linalg.inv(Q) @ c
print(x_star)

"""
print("Example 12.9")
Q = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 4]])
c = np.array([-8, -9, -8])
x_star = np.linalg.inv(Q) @ c
print(x_star)
"""

x0 = np.zeros_like(c)  # need to store this?
n, m = np.shape(Q)
B0 = np.eye(n)

print(quasi_newt_rank_one(x0, B0, Q, c))
