from typing import Callable

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optm

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


def func_one_derv(x: float) -> float:
    return 3 * x**2 - 2 * np.cos(x)


def func_two_derv(x: float) -> float:
    return 12 * x**3 - 12 * x**2 + 6 * x - 6


def secant_search(func: Callable, xkmo: float, xk: float) -> float:
    sec_top = -(xk - xkmo) * func(xk)
    sec_btm = func(xk) - func(xkmo)
    return sec_top / sec_btm


def secant(func: Callable, x0: float, x1: float, tol: float = 1e-8) -> tuple[float, int, list]:
    xlist = [x0, x1]
    k = 0
    while abs(func(xlist[-1])) > tol:
        pk = secant_search(func, xlist[-2], xlist[-1])
        xlist.append(xlist[-1] + pk)
        if k == 100:
            break
        k += 1
    return xlist[-1], k, xlist


def secant_error(xlist: list, x_star: float) -> tuple[np.ndarray, np.ndarray]:
    xray = np.asarray(xlist)
    ekpo = np.abs(xray[2:] - x_star)  # ek+1
    ek = np.abs(xray[1:-1] - x_star)
    return ek, ekpo


def log_model(log_ek, r, c):
    # c should be log(c)
    return r * log_ek + np.log(c)


def log_fit(ek, ekpo):
    log_ek = np.log(ek)
    log_ekpo = np.log(ekpo)
    params, covar = optm.curve_fit(
        log_model,
        log_ek,
        log_ekpo,
        p0=(1.61, 0.5),
    )
    r, c = params
    return r, c


x_star, k, xlist = secant(func_one_derv, 0, 1)
print(f"First Convergence at {x_star}")
ek, ekpo = secant_error(xlist, 0.7108)
sub = 3
ek, ekpo = ek[sub:], ekpo[sub:]
r, c = log_fit(ek, ekpo)
print(f"Convergence rate: {r:0.3f}, Coefficient: {c:0.3f}")
# plt.plot(ek, ekpo, label="linear")
# plt.plot(np.log(ek), np.log(ekpo), label="errors", marker=".")
# plt.legend()
# plt.show()
# print(secant(func_two_derv, -1, 0))

x_star, k, xlist = secant(func_two_derv, -1, 0)
print(f"Second Convergence at {x_star}")
ek, ekpo = secant_error(xlist, 1)
r, c = log_fit(ek, ekpo)
print(f"Convergence rate: {r:0.3f}, Coefficient: {c:0.3f}")
# plt.plot(ek, ekpo, label="linear")
plt.plot(np.log(ek), np.log(ekpo), marker=".")
plt.xlabel("Log(ek)")
plt.ylabel("Log(ek+1)")
plt.title("Log Fit of Errors for Problem 18 Part ii")
plt.savefig("figures/hw8_prob18.png", bbox_inches="tight")
# plt.show()
