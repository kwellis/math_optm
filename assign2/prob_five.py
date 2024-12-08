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


def func_alpha(x):
    return 9 * x - 14


def func_bravo(x):
    return 1 / (3 + x**4)


def func_charlie(x):
    if (1 + x**2) >= 0:
        f = np.sqrt(1 + x**2)
    else:
        f = np.nan
    return f


def func_delta(x):
    return np.abs(x)


x = np.linspace(-10, 10, 100)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(7, 5), sharex=True)

f_a = func_alpha(x)
f_b = func_bravo(x)
f_c = np.asarray([func_charlie(xi) for xi in x])
f_d = func_delta(x)

ax1.plot(x, f_a, label="alpha")
ax1.set_title("f(x) = 9x - 14")

ax2.plot(x, f_b, label="bravo")
ax2.set_title("f(x) = 1 / (3 + x**4)")

ax3.plot(x, f_c, label="charlie")
ax3.set_title("f(x) = sqrt(1 + x**2)")

ax4.plot(x, f_d, label="delta")
ax4.set_title("f(x) = abs(x)")

plt.savefig("figures/hw2_prob_5.png", bbox_inches="tight")
plt.show()

"""
Alpha, I would say the function has no convex or concavity

Bravo, Concave from -5 to 5. Outside that region it is flat, and the line sits on top of the function.

Charlie, Convex across the entire real line, meets the definition, blah, blah,
        Also, the second order derivative has positive values for all x values.
        Make sure to write in the second order derivative

Delta, Tough to say, because I don't think the absolute value is considered continuous?
        Ultimately the function is not differentiable when x = 0.
        Sounds like the function does not need to be continuous to be convex, Ed stated this in Monday lecture
        So the absolute value function would still be convex.
"""
