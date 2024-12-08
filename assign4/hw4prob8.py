import numpy as np


def check_indices(n_cols: int, m_rows: int, b_idx: list[int], n_idx: list[int]) -> None:
    """Check Columns / Index

    Check that the basic index and nonbasic index are represented inside the
    actual A matrix, eg a column 5 isn't specified in a 2x2 matrix. Also make
    sure that the b_idx and n_idx represent all the available columns.

    Args:
        n_cols (int): Number of Columns in A
        m_rows (int): Number of Rows in A
        b_idx (list[int]): Indices of the basic variables / columns
        n_idx (list[int]): Indices of the non-basic variables / columns

    Return:
        None
    """
    # check that the length of b is equal to the number of rows m
    if m_rows != len(b_idx):
        raise ValueError(f"Number of Columns in B: {len(b_idx)}, does not match rows in A: {m_rows}")

    # first, verify the same number doesn't appear in b_idx and n_idx
    if set(b_idx) & set(n_idx):
        raise ValueError(f"Overlap detected: Idx {set(b_idx) & set(n_idx)} appear in basic and nonbasic")

    # second, make sure all the columns are represented in b_idx or n_idx
    idx_set = set(b_idx + n_idx)
    n_set = set([*range(0, n_cols, 1)])

    if idx_set != n_set:
        raise ValueError(f"Columns are not totally represented in basic and nonbasic idx {n_set - idx_set}")

    return None


def reorder_idx(b_idx: list[int], n_idx: list[int]) -> list[int]:
    """Re Order the indices as required.

    Args:
        b_idx (list[int]): Indices of the basic variables / columns
        n_idx (list[int]): Indices of the non-basic variables / columns

    Returns:
        re_idx (list[int]): Reordered Indices for Shuffling
    """
    # Combine the basic and non-basic indices
    old_idx = b_idx + n_idx
    # Create the new order based on the combined indices
    re_idx = sorted(range(len(old_idx)), key=lambda i: old_idx[i])
    return re_idx


def nullmat(A: np.ndarray, b_idx: list[int], n_idx: list[int]) -> np.ndarray:
    """Null Basis Matrix

    Input a matrix A, the required basic indices and the nonbasic indices.
    Return the null basis matrix Z. Really only need to define the b_idx,
    the n_idx could be found from all the values not specified. The b_idx and
    the n_idx to not need to be specified in sequential order.

    Args:
        A (np.ndarray): Matrix A
        b_idx (list[int]): Indices of the basic variables / columns
        n_idx (list[int]): Indices of the non-basic variables / columns

    Returns:
        Z (np.ndarray): Null Basis Matrix Z
    """

    m, n = A.shape  # rows, columns (did I mess this up?)

    check_indices(n, m, b_idx, n_idx)

    B = A[:, b_idx]
    N = A[:, n_idx]

    zero_tol = 1e-3
    if abs(np.linalg.det(B) - 0) < zero_tol:
        raise ValueError("Determinent of B Matrix is Zero, Pick New Basic Index")

    B_inv = np.linalg.inv(B)
    top = np.dot(-1 * B_inv, N)
    id_mat = np.eye(len(n_idx))

    Z_tilde = np.vstack((top, id_mat))
    re_idx = reorder_idx(b_idx, n_idx)
    Z = Z_tilde[re_idx, :]
    return Z


if __name__ == "__main__":
    # this is Part I in 3.3.1
    a_mat = np.array([[1, 1, 1, 1], [1, -1, -1, 1], [0, 1, 0, 1]])
    b_idx = [0, 1, 2]  # define the 1st, 2nd and 3rd row indexs
    n_idx = [3]
    Z = nullmat(a_mat, b_idx, n_idx)
    print(f"Part I Check:\n {Z}")

    # this is Part II in 3.3.1
    a_mat = np.array([[1, 1, 1, 1]])
    b_idx = [0]  # define the 1st, 2nd and 3rd row indexs
    n_idx = [1, 2, 3]
    Z = nullmat(a_mat, b_idx, n_idx)
    print(f"Part II Check:\n {Z}")

    # this is Exercise 3.3.3
    a_mat = np.array([[1, 2, 0, 2], [2, 1, 2, 4]])
    b_idx = [1, 2]  # define the 1st, 2nd and 3rd row indexs
    n_idx = [0, 3]
    Z = nullmat(a_mat, b_idx, n_idx)
    print(f"Exercise 333 Check:\n {Z}")
