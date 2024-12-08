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

x1_min, x1_max = 0, 1.5
# plot the feasible region
d = np.linspace(x1_min, x1_max, 1000)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((x1 + x2 == 1) & (x1 >= 0) & (x2 >= 0)).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.9,
)

x_dict = {"xa": (0, 1), "xb": (1, 0), "xc": (1 / 2, 1 / 2)}

for x_key, x_val in x_dict.items():
    plt.scatter(x_val[0], x_val[1])
    plt.annotate(
        f"{x_val[0], x_val[1]}",
        xy=(x_val[0], x_val[1]),
        xycoords="data",
        xytext=(1.5, 1.5),
        textcoords="offset points",
    )

plt.title("Exercise 3.1.2 Feasible Set")
plt.xlabel("x1")
plt.ylabel("x2")
# plt.savefig("figures/exer312.png", bbox_inches="tight")
plt.show()
