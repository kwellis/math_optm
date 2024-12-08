import matplotlib.pyplot as plt
import numpy as np

from assign3.exer313 import max_step_size
from assign4.visual_aide import plot_inequalities

# Exercise 4.1.1 Part ii
A = np.array([[2, 1], [1, 1], [1, -3], [6, -1], [1, 0], [0, 1]])
B = np.array([12, 5, -3, 12, 0, 0])

xa = np.array([6, 0])
p1 = np.array([0, 1])
p2 = np.array([1, 0])

alpha1 = max_step_size(xa, p1, A, B)
alpha2 = max_step_size(xa, p2, A, B)

print(f"Alpha 1 is {alpha1}, Alpha 2 is {alpha2}")


def func_part2(x1, x2):
    return x1 + 2 * x2


# adding graphics
prob_name = "Problem 10 Part I"
file_name = "prob10i"
x1_range = (-1, 10)
x2_range = (-1, 10)
p_list = [p1, p2]
alpha_list = [3, np.inf]

plot_inequalities(
    A,
    B,
    x1_range,
    x2_range,
    func_part2,
    prob_name,
    file_name,
    show_feasible=True,
    xf=xa,
    p_list=p_list,
    alpha_list=alpha_list,
)

# Exercise 4.1.1 Part iii
A = np.array([[1, -2], [-1, -1], [1, 0], [0, 1]])
B = np.array([4, -8, 0, 0])

xb = np.array([8, 0])
p1 = np.array([-2, 1])
p2 = np.array([-np.pi, 0])

alpha1 = max_step_size(xb, p1, A, B)
alpha2 = max_step_size(xb, p2, A, B)

print(f"Alpha 1 is {alpha1}, Alpha 2 is {alpha2}")


def func_part3(x1, x2):
    return x1 - 2 * x2


# adding graphics
prob_name = "Problem 10 Part II"
file_name = "prob10ii"
x1_range = (-1, 10)
x2_range = (-1, 10)
p_list = [p1, p2]
alpha_list = [1.0, 1.27]

plot_inequalities(
    A,
    B,
    x1_range,
    x2_range,
    func_part2,
    prob_name,
    file_name,
    show_feasible=True,
    xf=xb,
    p_list=p_list,
    alpha_list=alpha_list,
)
