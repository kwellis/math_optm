import itertools

import numpy as np

# from assign4.visual_aide import plot_inequalities


def check_dims(A: np.ndarray, b: np.ndarray) -> None:
    """Check the dimensions

    Check the dimensions of the A matrix and b vector. Ensure the A matrix has
    full row rank. Make sure the number of rows in the A matrix match the rows
    in the b vector. Do some other stuff?

    Args:
        A (np.ndarray): A matrix that is n x m with m > n
        b (np.ndarray): b vector that is n long"""

    A_rows, A_cols = A.shape
    b_rows, b_cols = b.shape
    A_rank = np.linalg.matrix_rank(A)

    if A_cols <= A_rows:
        raise ValueError(f"Number of rows in A: {A_rows} is less or equal to columns: {A_cols}")

    if A_rows != b_rows:
        raise ValueError(f"Number of rows in b: {b_rows}, do not match number of rows in A: {A_rows}")

    if A_rank != A_rows:
        raise ValueError(f"Matrix A does not have full row rank: Rank is {A_rank} Rows are: {A_rows}")


def is_basic(B: np.ndarray) -> bool:
    """Is Basic

    Check to make sure the basis matrix B has columns that are all linearly independent
    from each other. If not return False, if yes return True

    Args:
        B (np.ndarray): B basis vector

    Returns:
        col_lin_ind (np.bool): Are the columns linearly independent or not
    """
    B_rows, B_cols = B.shape
    B_rank = np.linalg.matrix_rank(B)

    if B_rank != B_rows:
        col_lin_ind = False
    else:
        col_lin_ind = True

    return col_lin_ind


def is_feasible(x: np.ndarray) -> np.bool:
    """Is Feasible

    Check if the x array is feasible or not. Return True if feasible, false if not.
    Vector is feasible if all the values are greater than or equal to zero, x >= 0.

    Args:
        x (np.ndarray): x vector of values of x

    Returns:
        tot_feas (boolean): True if all scalars are greater or equal to zero, false other
    """
    one_feas = np.greater_equal(x, np.zeros_like(x))  # check if each element is greater or equal to zero
    tot_feas = np.all(one_feas)
    return tot_feas


def basic_solns(A: np.ndarray, b: np.ndarray) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Basic Solutions

    Input matrix A and vector b of the form Ax=b. The matrix A is a n x m matrix with
    m > n. Creates a series of indicies with all the different combinations possible
    and solves the values of xb, inserts xb back into x, with xn being described as
    zeroes, sorts through the list, looking for feasible and non feasible solutions.
    Splits up the list based on whether it is feasible or not.

    Args:
        A (np.ndarray): A matrix that is n x m with m > n
        b (np.ndarray): b vector that is n long

    Returns:
        xf (list): List of the feasible x values
        xnf (list): List of the non-feasible x values"""

    m_rows, n_cols = A.shape

    # create iterable object of various combinations
    xb_idxs = list(itertools.combinations(range(n_cols), m_rows))
    xf = []
    xnf = []

    for xb_idx in xb_idxs:
        B = A[:, xb_idx]
        if is_basic(B) is False:
            continue  # restart with next xb_idx
        xb = np.linalg.inv(B) @ b
        x = np.zeros((1, n_cols))  # create array of zeros
        x[:, xb_idx] = xb  # update x with values of x at proper indx

        if is_feasible(x):
            xf.append(x)
        else:
            xnf.append(x)

    # need to remove duplicates from xf, xnf
    return xf, xnf


if __name__ == "__main__":
    a_mat = np.array([[2, 1, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
    b_vec = np.array([100, 80, 40])

    xf, xnf = basic_solns(a_mat, b_vec)

    print("Basic Feasible Solutions:")
    for x in xf:
        print(x)
    print("Basic Solutions:")
    for x in xnf:
        print(x)

    # visualize the feasible set and solutions, double check codes
    prob_name = "Exercise 4.3.1"
    file_name = "exer431"

    # dummy function
    def func_part1(x1, x2):
        return x1 + x2

    a_vis = np.array([[-2, -1], [-1, -1], [-1, 0]])
    b_vis = b = np.array([-100, -80, -40])

    # Define the range for x1 and x2
    x1_range = (-0.5, 100)
    x2_range = (-0.5, 100)

    # Call the function
    # plot_inequalities(a_vis, b_vis, x1_range, x2_range, func_part1, prob_name, file_name)

    # exercise 4.3.12
    a_mat = np.array([[1, 4, 7, 1, 0, 0], [2, 5, 8, 0, 1, 0], [3, 6, 9, 0, 0, 1]])
    x_vec = np.array([1, 1, 1, 0, 0, 0])
    b_vec = np.array([12, 15, 18])

    B = a_mat[:, :3]
    print(f"Matrix Rank is {np.linalg.matrix_rank(B)}")
    print(f"Matrix Det is {np.linalg.det(B)}")

    print("Is it a solution?")
    print(a_mat @ x_vec)
