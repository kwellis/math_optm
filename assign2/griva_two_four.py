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


def fun_one_x2(x1):
    if (2 * x1 - x1**2) >= 0:
        x2 = np.sqrt(2 * x1 - x1**2)
    else:
        x2 = np.nan
    return x2


def fun_two_x2(x1):
    if (-2 * x1 - x1**2) >= 0:
        x2 = np.sqrt(-2 * x1 - x1**2)
    else:
        x2 = np.nan
    return x2


x1_min, x1_max = -3, 3

# plot the feasible region
d = np.linspace(x1_min, x1_max, 500)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    (((x1 - 1) ** 2 + x2**2 == 1) & ((x1 + 1) ** 2 + x2**2 == 1)).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.1,
)

x1 = np.linspace(x1_min, x1_max, 1000)
x2_one = np.asarray([fun_one_x2(x) for x in x1])
x2_two = np.asarray([fun_two_x2(x) for x in x1])

plt.plot(x1, x2_one, linestyle="", marker=".", color="b", label="$(x_{1} - 1)^{2} + x_{2}^{2} = 1$")
plt.plot(x1, -1 * x2_one, linestyle="", marker=".", color="b", label="_func_one")

plt.plot(x1, x2_two, linestyle="", marker=".", color="r", label="$(x_{1} + 1)^{2} + x_{2}^{2} = 1$")
plt.plot(x1, -1 * x2_two, linestyle="", marker=".", color="r", label="_func_two")

plt.xlabel("x1")
plt.ylabel("x2")

plt.title("Griva Exercise 2.4")
plt.legend()
plt.savefig("figures/hw2_exer_24.png", bbox_inches="tight")
plt.show()

"""
Answer: Two circles that only overlap at the point (0,0), so that is the feasible set. I would argue
that would be your local and global minimizer since that is the only point on the graph??? What else
can we say about it?
"""
