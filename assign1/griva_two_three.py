import matplotlib.pyplot as plt
import numpy as np


def fun_one(x1):
    if x1**2 <= 4:
        x2 = np.sqrt(4 - x1**2)
    else:
        x2 = np.nan
    return x2


d = np.linspace(-2, 2, 500)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((x1 >= 1) & (x2 >= -np.sqrt(4 - x1**2)) & (x2 <= np.sqrt(4 - x1**2))).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.1,
)


x1 = np.linspace(-2, 2, 100)
x2 = [fun_one(x) for x in x1]
x2 = np.asarray(x2)
plt.plot(x1, x2, marker=" ", linestyle="--", color="r", label="InEqual One")
plt.plot(x1, -1 * x2, marker=" ", linestyle="--", color="r")
plt.axvline(1, linestyle="--", label="InEqual Two")
plt.xlabel("x1")
plt.ylabel("x2")

plt.legend()
plt.title("Problem 2.3 Feasible Set. Local Minimizers at x1 = 1")
plt.show()
