import matplotlib.pyplot as plt
import numpy as np


# Define the plane equation x1 + x2 + x3 = 21
def fish_plane(x1, x3):
    return 21 - x1 - x3


# Create a meshgrid for plotting the plane
x1_vals = np.linspace(0, 2, 100)  # x2>=0 and x2<=2
x3_vals = np.linspace(4, 10, 100)  # x3>=4 and x3<=10
x1, x3 = np.meshgrid(x1_vals, x3_vals)
x2 = fish_plane(x1, x3)

# Plotting the 3D graph
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Plot the plane
ax.plot_surface(x1, x2, x3, color="cyan", alpha=0.75)  # , rstride=100, cstride=100)

ax.scatter(2, 15, 4, label="soln")

# set all the axis to the same length
ax.set_xlim([0, 21])
ax.set_ylim([0, 21])
ax.set_zlim([0, 21])

ax.set_xlabel("x1, Fresh Fish")
ax.set_ylabel("x2, Frozen Fish")
ax.set_zlabel("x3, Smoked Fish")

plt.legend()
plt.title("Solution at x1=2, x2=15, x3=4")
plt.show()

# plot the feasible region
d = np.linspace(-2, 21, 300)
x1, x2 = np.meshgrid(d, d)
plt.imshow(
    ((x1 >= 0) & (x1 <= 2) & (x1 + x2 <= 17) & (x1 + x2 >= 11)).astype(int),
    extent=(x1.min(), x1.max(), x2.min(), x2.max()),
    origin="lower",
    cmap="Greys",
    alpha=0.1,
)

x1 = np.arange(0, 21, 1)

x2_up = 17 - x1
x2_dn = 11 - x1
plt.plot(x1, x2_up)
plt.plot(x1, x2_dn)
plt.axhline(0)
plt.axvline(0)
plt.axvline(2)
plt.scatter(2, 15, linestyle="", marker="o", color="r", label="soln")

plt.xlabel("x1, Fresh Fish")
plt.ylabel("x2, Frozen Fish")

plt.title("Salmon Feasible State in 2D")
plt.legend()
plt.show()
