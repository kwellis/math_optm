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


def func(x1, x2):
    return (x1 - 1) ** 2 + (x2 + 1) ** 2


ax_lim = 5
spc = 0.01

x1_axis = np.arange(-ax_lim, ax_lim, spc)
x2_axis = np.arange(-ax_lim, ax_lim, spc)

[X1, X2] = np.meshgrid(x1_axis, x2_axis)

plt.figure(figsize=(4, 4))

plt.imshow(
    ((X1**2 + X2**2 <= 9) & (X2 >= 0)).astype(int),
    extent=(X1.min(), X1.max(), X2.min(), X2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.5,
)

CS = plt.contour(X1, X2, func(X1, X2), levels=[1, 4, 8, 16, 32, 48])

x_dict = {"A": (0, 0), "B": (0, 3), "C": (1, 0)}

for x_key, x_val in x_dict.items():
    plt.scatter(x_val[0], x_val[1])
    plt.annotate(
        f"{x_val[0], x_val[1]}",
        xy=(x_val[0], x_val[1]),
        xycoords="data",
        xytext=(1.5, 1.5),
        textcoords="offset points",
    )

plt.clabel(CS, inline=1, fontsize=10)
plt.title("Contour Plot for Problem 21")
plt.xlabel("x1")
plt.ylabel("x2")
plt.axis("equal")
plt.savefig("figures/hw9_prob21.png", bbox_inches="tight")
# plt.show()
