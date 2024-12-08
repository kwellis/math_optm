import numpy as np

from assign4.hw4prob8 import nullmat
from assign4.visual_aide import plot_inequalities
from assign5.exer431 import basic_solns

# Exercise 4.1.1 Part I
prob_name = "Exercise 4.3.4"
file_name = "exer434"


def func_part1(x1, x2):
    return -5 * x1 - 7 * x2


A = np.array([[3, -2], [2, -1], [1, 0], [0, 1]])
b = np.array([-30, -12, 0, 0])

# Define the range for x1 and x2
x1_range = (-0.5, 60)
x2_range = (-0.5, 60)

# Call the function
plot_inequalities(A, b, x1_range, x2_range, func_part1, prob_name, file_name)

# writing everything in standard form
A = np.array([[-3, 2, 1, 0], [-2, 1, 0, 1]])
b = np.array([30, 12])

xf, xnf = basic_solns(A, b)

print("Basic Feasible Solutions:")
for x in xf:
    print(x)
print("Basic Solutions:")
for x in xnf:
    print(x)

b_idx = [0, 2]
n_idx = [1, 3]

Z = nullmat(A, b_idx, n_idx)

print(f"Null Basis of A:\n{Z}")

# confirming they work
d1 = np.array([0.5, 0, 1.5, 1])
d2 = np.array([2, 3, 0, 1])

print("Confirm Solutions:")
print(A @ d1)
print(A @ d2)
