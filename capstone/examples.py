import numpy as np
from network import newton_reduced, optimality_test, qr_split
from ratio_test import ratio_test

"""
# example 3.4, ratio test, page 81
a_mat = np.array([[1, 4], [0, 3], [5, 1]])
b_vec = np.array([3, 2, 4])
xe = np.array([1, 1])
pe = np.array([4, -2])
inact_con = np.array([4, 6, 10])

alpha_e = ratio_test(xe, pe, a_mat, b_vec, inact_con)
print(alpha_e)
"""

"""
# example 15.1, reduced Newton Direction, page 551
dfk = np.array([8, 2, 0])
Z = np.array([[1, 1], [1, 0], [0, 1]])
Hfk = np.array([[1, 4, 3], [4, 0, -2], [3, -2, -1]])
p = newton_reduced(dfk, Hfk, Z)
p_book = np.array([-4 / 3, -2 / 3, -2 / 3])
print(f"Kaelin Answer: {p} \nBook Answer: {p_book}")
"""


# example 15.4, QR Factor for Null and Ar, page 559
A = np.array([[1, -1, 0, 0], [0, 0, 1, 1]])
Z, Ar = qr_split(A)
print(Z)
print(Ar)

"""
# example 15.7, swap variables, page 567
A = np.array([[2, -1], [0, 1]])
dfk = np.array([-3, -4])
Z, Ar = qr_split(A)
W = np.array([True, False, True])
opt, active, con_updt = optimality_test(dfk, Z, Ar, W)
print(opt, active, con_updt)
"""
