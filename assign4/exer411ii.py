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
def f(x1, x2):
    return x1 + 2 * x2


x1_min, x1_max = -0.5, 10
# plot the feasible region
d = np.linspace(x1_min, x1_max, 500)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((2 * x1 + x2 >= 12) & (x1 + x2 >= 5) & (-x1 + 3 * x2 <= 3) & (6 * x1 - x2 >= 12) & (x1 >= 0) & (x2 >= 0)).astype(
        int
    ),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.1,
)

Z = f(x1, x2)
contour_levels = np.linspace(Z.min(), Z.max(), 20)  # Create 10 contour levels
contour = plt.contour(x1, x2, Z, levels=contour_levels, cmap="coolwarm", linestyles="dashed")

plt.colorbar(contour, label="f(x1, x2) Value")

plt.title(f"{filename} Maximization Problem")
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig(f"figures/hw4_{filename}.png", bbox_inches="tight")
plt.show()
