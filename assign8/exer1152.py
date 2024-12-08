def func(x1: float, x2: float) -> float:
    return 2 * x1**2 + x2**2 - 2 * x1 * x2 + 2 * x1**3 + x1**4


print("First Value:")
print(func(0, -1))

print("\nSecond Value:")
print(func(0, -2))
