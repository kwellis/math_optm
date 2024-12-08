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
    return 5 * x1**4 + 6 * x2**4 - 6 * x1**2 + 2 * x1 * x2 + 5 * x2**2 + 15 * x1 - 7 * x2 + 13


def derv_xone(x1: float, x2: float) -> float:
    return 20 * x1**3 - 12 * x1 + 2 * x2 + 15


def derv_xtwo(x1: float, x2: float) -> float:
    return 24 * x2**3 + 10 * x2 + 2 * x1 - 7


def grady(x1: float, x2: float) -> np.ndarray:
    return np.array([derv_xone(x1, x2), derv_xtwo(x1, x2)])


def hessy(x1: float, x2: float) -> np.ndarray:
    return np.array([[60 * x1**2 - 12, 2], [2, 72 * x2**2 + 10]])


def newty(x1: float, x2: float, tol: float = 1e-6) -> tuple[float, float]:
    while abs(derv_xone(x1, x2)) > tol and abs(derv_xtwo(x1, x2)) > tol:
        x1, x2 = np.array([x1, x2]) - np.linalg.inv(hessy(x1, x2).T) @ grady(x1, x2)
    return x1, x2


x1_opt, x2_opt = newty(1, 1)
print(x1_opt, x2_opt)

print(np.linalg.eigvals(hessy(x1_opt, x2_opt)))

d1 = np.linspace(-2, 0, 250)
d2 = np.linspace(-0.5, 1.5, 250)
x1, x2 = np.meshgrid(d1, d2)

Z = base_func(x1, x2)  # type: ignore
contour_levels = np.linspace(Z.min(), Z.max(), 20)  # type: ignore
contour = plt.contour(x1, x2, Z, levels=contour_levels, cmap="coolwarm", linestyles="dashed")

plt.colorbar(contour, label="f(x1, x2) Value")

plt.title("Exercise 11.3.3 Function")
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("figures/hw7_exer1133.png", bbox_inches="tight")
# plt.show()
