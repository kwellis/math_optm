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
    return x**3 - 5 * x**2 - 12 * x + 19


def func_prime(x: float) -> float:
    return 3 * x**2 - 10 * x - 12


def newty(x_guess: float) -> float:
    i = 0
    while abs(func(x_guess)) > 0.00001:
        x_guess = x_guess - func(x_guess) / func_prime(x_guess)
        print(i, x_guess)
        i += 1
    return x_guess


x_guess = np.array([-2, 2, 6])  # guesses to start the iteration on

print("The exact roots are:")
for x in x_guess:
    print(newty(x))

x = np.linspace(-3, 7, 100)
y = func(x)

plt.plot(x, y)
plt.axhline(y=0, color="r", linestyle="--")
plt.title("Visualize Function of Exercise 2.7.1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig(f"figures/hw6_{filename}.png", bbox_inches="tight")
# plt.show()
