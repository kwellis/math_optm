import matplotlib.pyplot as plt
import numpy as np


def func(x):
    f = (x**2 + np.sin(x)) ** 2 - 10 * (np.cos(5 * x) + 3 * x / 2)
    return f


def func_first_derv(x):
    fp = 2 * (x**2 + np.sin(x)) * (2 * x + np.cos(x)) + 50 * np.sin(5 * x) - 15
    return fp


def secant(xvar1: float, xvar2: float, fvar1: float, fvar2: float) -> float:
    """Secant Method

    Uses the secant method to calculate the next fprime to use to find a zero.

    Args:
        xvar1 (float): x value one
        xvar2 (float): x value two
        fvar1 (float): Function value at x one
        fvar2 (float): Function value at x two

    Return:
        xvar3 (float): x value three
    """
    xvar3 = xvar2 - fvar2 * (xvar1 - xvar2) / (fvar1 - fvar2)
    return xvar3


x = np.linspace(0, 2, 60)
f = func(x)

plt.scatter(x, f, label="f(x)", marker="v")
plt.xlabel("x values")
plt.ylabel("F(x)")
plt.legend()
plt.show()

fmin_idx = np.argmin(f)

x_list = [x[fmin_idx], x[fmin_idx + 1]]
fp_list = [func_first_derv(x[fmin_idx]), func_first_derv(x[fmin_idx + 1])]

err = 0.01  # acceptable error amount
while abs(fp_list[-1] - fp_list[-2]) > err:
    x_list.append(secant(x_list[-2], x_list[-1], fp_list[-2], fp_list[-1]))
    fp_list.append(func_first_derv(x_list[-1]))

for x, fp in zip(x_list, fp_list):
    print(f"X Value: {x}, F-Prime Value: {fp}")

fmin_actual = func(x_list[-1])
print("\n")
print(f"Minimal value for the function is {fmin_actual}")
