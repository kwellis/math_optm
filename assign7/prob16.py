import numpy as np


def func(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> np.ndarray:
    return 1 / 2 * x.T @ Q @ x - c.T @ x


def grad(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> np.ndarray:
    return Q @ x - c


def hess(Q: np.ndarray) -> np.ndarray:
    return Q


def alpha_quad(x: np.ndarray, Q: np.ndarray, c: np.ndarray) -> float:
    a_top = grad(x, Q, c).T @ grad(x, Q, c)
    a_btm = grad(x, Q, c).T @ Q @ grad(x, Q, c)
    return float(a_top / a_btm)


def sdquad(x0: np.ndarray, Q: np.ndarray, c: np.ndarray, tol: float = 1e-8) -> tuple[np.ndarray, np.ndarray, int]:
    xk = x0
    max_iter = 1000
    for k in range(0, max_iter):
        dfk = grad(xk, Q, c)  # first derivative
        if np.linalg.norm(dfk) < tol:
            break
        pk = -dfk  # search direction
        alpha = alpha_quad(xk, Q, c)
        xk = xk + alpha * pk
    return func(xk, Q, c), xk, k


# part b, example 12.1
print("Part B")
Q = np.array([[1, 0, 0], [0, 5, 0], [0, 0, 25]])
c = np.array([-1, -1, -1])
x0 = np.array([0, 0, 0])
print(np.linalg.eig(Q))
print(sdquad(x0, Q, c))
print(f"Condition of Matrix: {np.linalg.cond(Q)}")

# part c
print("Part C")
Q = np.array([[2.3, 0.19, -0.89], [0.19, 1.84, 0.32], [-0.89, 0.32, 1.86]])
eigval, eigvec = np.linalg.eig(Q)
print(eigval)
print(eigvec)
print(Q @ eigvec[:, 0].T)  # so an eigenvalue of one...da fuq?
print(Q @ eigvec[:, 2].T)  # so an eigenvalue of one...da fuq?
print(sdquad(x0, Q, c))
print(f"Condition of Matrix: {np.linalg.cond(Q)}")
