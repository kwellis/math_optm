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


# code for updating graph
def feasible_point_direction_alpha(
    ax: plt.axes, xf: np.ndarray, p_list: list[np.ndarray], alpha_list: list[float]
) -> None:
    """Plot Feasible Point, Direction and Alpha

    Args:
        ax (axes): Matplotlib Axis
        xf (np array): Feasible Point
        p_list (list): List of Feasible Directions
        alpha_list (list): List of feasible step size

    Returns
        None
    """
    ax.plot(xf[0], xf[1], "ro")  # red point for feasible point
    ax.annotate(
        f"({xf[0]:.1f}, {xf[1]:.1f})",
        xy=(xf[0], xf[1]),
        xytext=(-1, -10),  # adjust as necessary textcoords="offset points",
        textcoords="offset points",
        ha="center",
    )

    for p_dir, alpha in zip(p_list, alpha_list):
        ax.quiver(xf[0], xf[1], p_dir[0], p_dir[1], angles="xy", scale_units="xy", scale=1, color="b")
        dir_str = f"p:({p_dir[0]:.1f}, {p_dir[1]:.1f})"

        ax.annotate(
            dir_str,
            xy=(xf[0] + p_dir[0], xf[1] + p_dir[1]),
            xytext=(0.5, 0),  # adjust as necessary textcoords="offset points",
            textcoords="offset points",
            ha="left",
        )

        if alpha != np.inf:
            alp_pnt = xf + alpha * p_dir
            ax.plot(alp_pnt[0], alp_pnt[1], "bo")  # red point for feasible point
            ax.annotate(
                f"ap+x:\n({alp_pnt[0]:.1f}, {alp_pnt[1]:.1f})",
                xy=(alp_pnt[0], alp_pnt[1]),
                xytext=(-1, 0.5),  # adjust as necessary textcoords="offset points",
                textcoords="offset points",
                ha="right",
            )


# Function to plot inequalities in the form Ax >= b
def plot_inequalities(
    A, b, x1_range, x2_range, func, prob, file_name, show_feasible=False, xf=None, p_list=None, alpha_list=None
):
    # Create a grid for x1 and x2
    x1_min, x1_max = x1_range
    x2_min, x2_max = x2_range
    x = np.linspace(x1_min, x1_max, 500)
    x1, x2 = np.meshgrid(x, x)  # Create a grid for x1 and x2 values

    fig, ax = plt.subplots(figsize=(5, 4))

    masks = []

    # Iterate through each inequality in Ax >= b
    for i, (a, b_i) in enumerate(zip(A, b)):
        inequality_mask = a[0] * x1 + a[1] * x2 >= b_i
        masks.append(inequality_mask)

        if a[1] != 0:  # If a[1] is non-zero, solve for x2
            x2_line = (b_i - a[0] * x) / a[1]
            ax.plot(x, x2_line, linestyle="-", label=f"${a[0]}*x1 + {a[1]}*x2 \geq {b_i}$")
        else:  # If a[1] == 0, plot a vertical line at x1 = b_i/a[0]
            ax.axvline(b_i / a[0], linestyle="-", label=f"${a[0]}*x1 + {a[1]}*x2 \geq {b_i}$")

        ax.imshow(
            inequality_mask.astype(int),
            extent=(x1_min, x1_max, x2_min, x2_max),
            origin="lower",
            cmap="Greys",
            alpha=0.05,
        )

    # Combine all masks into a single feasible region
    feasible_region = np.logical_and.reduce(masks)

    # Use imshow to display the feasible region
    ax.imshow(
        feasible_region.astype(int), extent=(x1_min, x1_max, x2_min, x2_max), origin="lower", cmap="Greys", alpha=0.4
    )

    Z = func(x1, x2)
    contour_levels = np.linspace(Z.min(), Z.max(), 20)  # Create 10 contour levels
    contour = ax.contour(x1, x2, Z, levels=contour_levels, cmap="coolwarm", linestyles="dotted")

    fig.colorbar(contour, ax=ax, label="f(x1, x2) Value")

    ax.set_xlim(x1_min, x1_max)
    ax.set_ylim(x2_min, x2_max)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.legend(loc="upper right")
    ax.set_title(f"Feasible Set and Function for {prob}")

    if show_feasible and xf is not None and p_list is not None and alpha_list is not None:
        feasible_point_direction_alpha(ax, xf, p_list, alpha_list)

    plt.savefig(f"figures/hw4_{file_name}.png", bbox_inches="tight")
    # plt.show()
