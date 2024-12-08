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


def base_func(x1: float, x2: float) -> float:
    return (x2 - x1**2) * (x2 - 2 * x1**2)


x1_min, x1_max = -0.5, 0.5
d = np.linspace(x1_min, x1_max, 500)
x1, x2 = np.meshgrid(d, d)

Z = base_func(x1, x2)  # type: ignore
contour_levels = np.linspace(Z.min(), Z.max(), 10)  # type: ignore
contour = plt.contour(x1, x2, Z, levels=contour_levels, cmap="coolwarm", linestyles="dashed")

plt.colorbar(contour, label="f(x1, x2) Value")

plt.title("Exercise 11.2.7 Function")
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("figures/hw7_exer1127.png", bbox_inches="tight")
# plt.show()
