import numpy as np


def func_one(x1: float, x2: float) -> float:
    return x1**2 + x2**2 - 1


def func_two(x1: float, x2: float) -> float:
    return 5 * x1**2 - x2 - 2


def funky(x1: float, x2: float) -> np.ndarray:
    return np.array([func_one(x1, x2), func_two(x1, x2)])


def grady(x1: float, x2: float) -> np.ndarray:
    return np.array([[2 * x1, 10 * x1], [2 * x2, -1]])


def newty(x1: float, x2: float) -> tuple[float, float]:
    while abs(func_one(x1, x2)) > 0.0001 and abs(func_two(x1, x2)) > 0.0001:
        print(x1, x2)
        x1, x2 = np.array([x1, x2]) - np.linalg.inv(grady(x1, x2).T) @ funky(x1, x2)
    return x1, x2


print(newty(1, 1))
print(newty(-1, -1))
print(newty(-1, 1))
print(newty(1, -1))

x_actual = [(0.732, 0.681), (-0.473, -0.881), (-0.732, 0.681), (0.473, -0.881)]

for x in x_actual:
    print(func_one(x[0], x[1]))
    print(func_two(x[0], x[1]))
