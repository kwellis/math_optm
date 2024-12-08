import matplotlib.pyplot as plt
import numpy as np

xf = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
yf = [4.914, 3.666, 2.289, 1.655, 1.029, 0.739, 0.393, 0.09, -0.197, -0.721, -0.971]


def func(xj, c1, c2, c3):
    g = c1 + c2 * xj + c3 * np.exp(-3 * xj)
    return g


# coefficients are found below
yfit = [func(x, 0.33271371, -1.37673055, 4.520509) for x in xf]

plt.scatter(xf, yf, label="data")
plt.plot(xf, yfit, linestyle="--", color="r", label="fit")
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.show()


def coeff_deriv(xj):
    dc1, dc2, dc3 = 1, xj, np.exp(-3 * xj)
    return dc1, dc2, dc3


def jacobian(x_ray):
    j_mat = np.empty([len(x_ray), 3])
    for i, xi in enumerate(x_ray):
        dc1, dc2, dc3 = coeff_deriv(xi)
        j_mat[i, 0] = dc1
        j_mat[i, 1] = dc2
        j_mat[i, 2] = dc3
    return j_mat


big_A = jacobian(xf)
A_inv = np.linalg.inv(np.matmul(big_A.T, big_A))
A_fin = np.matmul(A_inv, big_A.T)
x_hat = np.matmul(A_fin, np.array(yf))
print(x_hat)
