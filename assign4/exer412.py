import os

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

filename = os.path.splitext(os.path.basename(__file__))[0]


# function you are trying to minimize
def f(x1, x2, alpha):
    return alpha * x1 + (2 - alpha) * x2


def c1(x1):
    return -4 * x1 / 3


def c2(x1):
    return (7 - 2 * x1) / 3


def c3(x1):
    return 1 - x1


constraints = [
    (c1, "$4 * x1 + 3 * x2 \leq 0$", "-"),
    (c2, "$2 * x1 + 3 * x2 \leq 12$", ":"),
    (c3, "$x1 + x2 \leq 1$", "-"),
]

plt.figure(figsize=(5, 4))

x1_min, x1_max = -10, 10
# plot the feasible region
d = np.linspace(x1_min, x1_max, 500)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((4 * x1 + 3 * x2 <= 0) & (2 * x1 + 3 * x2 <= 12) & (x1 + x2 <= 1)).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.3,
)

x1_vals = np.linspace(x1_min, x1_max, 500)
for constraint_func, label, line in constraints:
    plt.plot(x1_vals, constraint_func(x1_vals), label=label, linestyle=line)

x_dict = {"xa": (-3, 4)}

for x_key, x_val in x_dict.items():
    plt.scatter(x_val[0], x_val[1])
    plt.annotate(
        f"{x_val[0], x_val[1]}",
        xy=(x_val[0], x_val[1]),
        xycoords="data",
        xytext=(1.5, 1.5),
        textcoords="offset points",
    )

alpha = 15 / 14
Z = f(x1, x2, alpha)
contour_levels = np.linspace(Z.min(), Z.max(), 10)  # Create 10 contour levels
contour = plt.contour(x1, x2, Z, levels=contour_levels, cmap="coolwarm", linestyles="dashed")

plt.colorbar(contour, label="f(x1, x2) Value")

plt.title(f"{filename} Maximization Problem, Alpha at 15/14")
plt.xlim(x1_min, x1_max)
plt.ylim(x1_min, x1_max)
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.savefig(f"figures/hw4_{filename}.png", bbox_inches="tight")
# plt.show()

"""The two active constraints are x1 + x2 <= 1 and 4x1 + 3x2 <= 0. You need to have an alpha that make the objective
function almost parallel to these constraints, but not quite. For the first value, if alpha is one, you are parallel.
Solve the ratio that (a/(2-a) = (1/1)) which is satisfied when alpha equals one. The second active constraint is
when (a/(2-a) = (4/3)), when you solve for the value of alpha, you get 8/7. So I would say alpha needs to be less than
8/7 and greater than 7/7 or 1."""
