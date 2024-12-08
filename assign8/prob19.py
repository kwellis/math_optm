import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

params = {
    "font.family": "serif",
    "font.serif": "cmr10",
    "font.sans-serif": "cmss10",
    "font.monospace": "cmtt10",
    "font.size": 10,
    "axes.formatter.use_mathtext": True,
    "axes.titlesize": "medium",
    "legend.frameon": False,
    "figure.dpi": 300,
}
mpl.rcParams.update(params)

print("Problem 19")
Q = np.array([[2, 0], [0, 4]])
c = np.array([3, 0])

x_star = np.linalg.inv(Q) @ c
print(x_star)

print("Condition of the Matrix")
print(np.linalg.cond(Q))


def func(x1, x2):
    return x1**2 + 2 * x2**2 - 3 * x1


ax_lim = 5
spc = 0.1

x1_axis = np.arange(-ax_lim, ax_lim, spc)
x2_axis = np.arange(-ax_lim, ax_lim, spc)

[X1, X2] = np.meshgrid(x1_axis, x2_axis)

plt.figure(figsize=(4, 4))

CS = plt.contour(X1, X2, func(X1, X2), levels=10)
plt.clabel(CS, inline=1, fontsize=10)
plt.title("Contour Plot for Problem 19")
plt.xlabel("x1")
plt.ylabel("x2")
plt.axis("equal")
plt.savefig("figures/hw8_prob19.png", bbox_inches="tight")
# plt.show()
