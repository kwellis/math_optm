import numpy as np
from visual_aide import plot_inequalities

# Exercise 4.1.1 Part I
prob_name = "Exercise 4.1.1 Part I"
file_name = "exer411i"


def func_part1(x1, x2):
    return 3 * x1 + x2


A = np.array([[-1, 1], [-3, -2], [-2, -3], [-2, 3], [1, 0], [0, 1]])
b = np.array([1, 12, -3, 9, 0, 0])

# Define the range for x1 and x2
x1_range = (-0.5, 5)
x2_range = (-0.5, 5)

# Call the function
plot_inequalities(A, b, x1_range, x2_range, func_part1, prob_name, file_name)

# Exercise 4.1.1 Part II
prob_name = "Exercise 4.1.1 Part II"
file_name = "exer411ii"


def func_part2(x1, x2):
    return x1 + 2 * x2


A = np.array([[2, 1], [1, 1], [1, -3], [6, -1], [1, 0], [0, 1]])
b = np.array([12, 5, -3, 12, 0, 0])

# Define the range for x1 and x2
x1_range = (-0.5, 10)
x2_range = (-0.5, 10)

# Call the function
plot_inequalities(A, b, x1_range, x2_range, func_part2, prob_name, file_name)


# Exercise 4.1.1 Part III
prob_name = "Exercise 4.1.1 Part III"
file_name = "exer411iii"


def func_part3(x1, x2):
    return x1 - 2 * x2


A = np.array([[1, -2], [-1, -1], [1, 0], [0, 1]])
b = np.array([4, -8, 0, 0])

# Define the range for x1 and x2
x1_range = (-0.5, 10)
x2_range = (-0.5, 10)

# Call the function
plot_inequalities(A, b, x1_range, x2_range, func_part3, prob_name, file_name)

# Exercise 4.1.1 Part IV
prob_name = "Exercise 4.1.1 Part IV"
file_name = "exer411iv"


def func_part4(x1, x2):
    return -x1 - x2


A = np.array([[1, -1], [1, -2], [1, 0], [0, 1]])
b = np.array([1, 12, 0, 0])

# Define the range for x1 and x2
x1_range = (-0.5, 20)
x2_range = (-0.5, 20)

# Call the function
plot_inequalities(A, b, x1_range, x2_range, func_part4, prob_name, file_name)
