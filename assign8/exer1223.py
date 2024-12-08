import numpy as np


def alpha(x1, x2):
    atop = x1**2 + 4 * x2**2
    abtm = 2 * x1**2 + 16 * x2**2
    return atop / abtm


def search(x1, x2):
    return np.array([-2 * x1, -4 * x2])


def steep_descent(x1, x2, ak, pk):
    return np.array([x1, x2]) + ak * pk


# first iteration
x1_0, x2_0 = 2, 1

ak = alpha(x1_0, x2_0)
pk = search(x1_0, x2_0)

x1_1, x2_1 = steep_descent(x1_0, x2_0, ak, pk)

print(ak)
print(pk)
print(x1_1, x2_1)

akp1 = alpha(x1_1, x2_1)
print(f"ak+1 {akp1}")
print(f"Gradient {search(x1_1, x2_1)}")

ak = alpha(x1_1, x2_1)
pk = search(x1_1, x2_1)
x1_2, x2_2 = steep_descent(x1_1, x2_1, ak, pk)
print(x1_2, x2_2)

print("Look at Lemma 12.4")
Q = np.array([[2, 0], [0, 4]])

cond_q = np.linalg.cond(Q)
err = ((cond_q - 1) / (cond_q + 1)) ** 2
print(f"Condition of Q: {cond_q}")
print(f"Error Boundary is: {err}")
