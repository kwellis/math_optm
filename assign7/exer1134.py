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


def func(x: float) -> float:
    return x**4 - 1


def func_prime(x: float) -> float:
    return 4 * x**3


def func_dprime(x: float) -> float:
    return 12 * x**2


def newty(x_guess: float) -> float:
    i = 0
    while abs(func_prime(x_guess)) > 0.00001:
        print(f"Loop: {i}, x: {x_guess:0.3f}, f(x): {func(x_guess):0.3f}")
        x_guess = x_guess - func_prime(x_guess) / func_dprime(x_guess)
        i += 1
        if i == 4:
            break
    return x_guess


print(newty(4))

x = np.linspace(-4.5, 4.5, 100)
y = func(x)  # type: ignore

plt.plot(x, y)
plt.axhline(y=0, color="r", linestyle="--")
plt.title("Visualize Function of Exercise 11.3.4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig(f"figures/hw7_{filename}.png", bbox_inches="tight")
# plt.show()
