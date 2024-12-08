import matplotlib.pyplot as plt
import numpy as np


def fun_one(x1, x2):
    out = 1 - x1**2 - x2**2
    return out


def fun_two(x1, x2):
    out = np.sqrt(2) - x1 - x2
    return out


def fun_one_x2(x1):
    if x1**2 <= 1:
        x2 = np.sqrt(1 - x1**2)
    else:
        x2 = np.nan
    return x2


def fun_two_x2(x1):
    x2 = np.sqrt(2) - x1
    return x2


# graph the shared region to see
d = np.linspace(-1.5, 1.5, 500)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((fun_one(x1, x2) >= 0) & (fun_two(x1, x2) >= 0) & (x2 >= 0)).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.1,
)

prop_cycle = plt.rcParams["axes.prop_cycle"]
colors = prop_cycle.by_key()["color"]

# graph the lines to see
x1 = np.linspace(-1.5, 1.5, 900)  # bump up to 900 to ensure the correct point is graphed
x2 = np.asarray([fun_one_x2(x) for x in x1])
plt.plot(x1, x2, marker=" ", linestyle="--", label="InEqual One", color=colors[0])
plt.plot(x1, -x2, marker=" ", linestyle="--", label="_InEqual One", color=colors[0])

x2 = np.asarray([fun_two_x2(x) for x in x1])
plt.plot(x1, x2, marker=" ", linestyle="--", label="InEqual Two", color=colors[1])

x2 = np.zeros_like(x1)
plt.plot(x1, x2, marker=" ", linestyle="--", label="InEqual Three", color=colors[2])

boundary_err = 0.0001  # floating point math checks


# categorize the points
def feasible_region(x):

    if abs(fun_one(x[0], x[1]) - 0) <= boundary_err:
        r_one = "Boundary"
    elif fun_one(x[0], x[1]) > 0:
        r_one = "Interior"
    else:
        r_one = "Exterior"

    if abs(fun_two(x[0], x[1]) - 0) <= boundary_err:
        r_two = "Boundary"
    elif fun_two(x[0], x[1]) > 0:
        r_two = "Interior"
    else:
        r_two = "Exterior"

    if x[1] == 0:
        r_thr = "Boundary"
    elif x[1] > 0:
        r_thr = "Interior"
    else:
        r_thr = "Exterior"
    return (
        float(fun_one(x[0], x[1])),
        float(fun_two(x[0], x[1])),
        float(x[1]),
        r_one,
        r_two,
        r_thr,
    )


x_dict = {"xa": (0.5, 0.5), "xb": (1, 0), "xc": (-1, 0), "xd": (-1 / 2, 0), "xe": (1 / np.sqrt(2), 1 / np.sqrt(2))}

sformat = "{:>6} | {:>6} | {:>6} | {:>8} | {:>8} | {:>8} \n"  # string format
nformat = "{:>6} | {:>6.3f} | {:>6.3f} | {:>8} | {:>8} | {:>8} \n"  # number format
spc = 58 * "-" + "\n"  # spacing

pout = sformat.format("Point", "x1", "x2", "InEq One", "InEq Two", "x2>=0") + spc

sig_fig = 4
i = 3
for x_key, x_val in x_dict.items():
    plt.scatter(x_val[0], x_val[1], color=colors[i])
    plt.annotate(x_key, xy=(x_val[0], x_val[1]), xycoords="data", xytext=(1.5, 1.5), textcoords="offset points")
    one_val, two_val, thr_val, one_id, two_id, thr_id = feasible_region(x_val)
    pout += nformat.format(x_key, x_val[0], x_val[1], one_id, two_id, thr_id)
    i += 1
print(pout)

plt.title("Griva 2.1 Feasibility Set")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.show()
