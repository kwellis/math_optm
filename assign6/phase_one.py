import numpy as np
import simplex as sx


def slack_index(col_vals: np.ndarray, col_idx: int) -> tuple[int, int] | None:
    """Slack Index

    Provide a column, this returns whether it meets the definition
    of a slack column, and which row it is associated with.

    Args:
        a_col (np.ndarray): Column of A matrix to evaluate
    """
    if np.count_nonzero(col_vals) == 1 and np.all((col_vals == 0) | (col_vals == 1)):
        row_idx = int(np.argmax(col_vals))
        return row_idx, col_idx  # row position
    return None


def slack_indices(A: np.ndarray) -> list:
    """Slack indices

    Provide a matrix A, identify which columns are slack columns
    meaning only one row is a positive one and the rest are zeros
    The matrix A needs to be in standard form.

    Args:
        A (np.ndarray): A matrix of variable coefficients

    Returns:
        slack_cols (list): List of slack columns that already exist
    """
    n, m = A.shape
    slack_idxs = []
    for i in range(m):  # iterate row by row
        slack_idxs.append(slack_index(A[:, i], i))
    slack_idxs = [x for x in slack_idxs if x is not None]
    return slack_idxs


def artificial_vars(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, list]:
    """Artificial Variables

    Provide a matrix A, add on rows with the necessary artificial
    columns. Identifies what already has slack variables on it. Adds
    artificial variables in the correct location as required.

    Args:
        A (np.ndarray): A matrix of variable coefficients

    Returns:
        artif_A (np.ndarray): A matrix with required artifical coeff
        artif_c (np.ndarray): c vector with required artifical coeff
        artif_x (np.ndarray): x vector with required artifical coeff
        artif_cols (list): List of artifical columns
    """
    n, m = A.shape

    slack_idxs = slack_indices(A)
    if len(slack_idxs) != 0:
        slack_rows, slack_cols = zip(*slack_idxs)
    else:
        slack_rows, slack_cols = [], []
    artif_count = n - len(slack_cols)  # how many artifical columns need to be added

    artif_A = np.hstack((A, np.zeros((n, artif_count))))
    artif_c = np.zeros((1, m))
    artif_x = np.zeros((1, m))

    for s_row, s_col in zip(slack_rows, slack_cols):
        artif_x[:, s_col] = 1

    artif_rows = list(set(range(n)) - set(slack_rows))
    artif_cols = list(set(range(m, m + artif_count, 1)) - set(slack_cols))
    for a_row, a_col in zip(artif_rows, artif_cols):
        artif_A[a_row, a_col] = 1
        artif_c = np.append(artif_c, 1)
        artif_x = np.append(artif_x, 1)

    return artif_A, artif_c, artif_x, artif_cols


def phaseone(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Phase One

    Solve phase one of the simplex problem to find a basic
    feasible solution. Need to add some error handling if a
    BFS cannot be found to start with.

    Args:
        A (np.ndarray): Rawr
        b (np.ndarray): Rawr

    Returns:
        x_bfs (np.ndarray): Basic Feasible Soln that can be used.
    """

    art_A, art_c, art_x, art_cols = artificial_vars(A)
    x, z, k = sx.sfsimplex(art_c, art_A, b, art_x, showiters=True)

    # if z cannot be driven down to zero with the simplex method
    if np.allclose(z, np.zeros_like(z)) is False:
        raise ValueError(f"The matrix:\n{A} and column:\n{b} have no feasible set")

    x_bfs = np.delete(x, art_cols, axis=0)  # delete artifical variables
    return x_bfs


"""A = np.array([[3, 2, 0, 0], [2, -4, -1, 0], [4, 3, 0, 1]])
b = np.array([14, 2, 19])
x_bfs = np.array([4, 1, 2, 0])

print(phaseone(A, b))
print(A @ x_bfs)  # looks good to me"""

# salmon problem, need to document writing in standard form, instead of hap-hazard
sal_A = np.array([[1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1]])
sal_b = np.array([17, 2, 10])
sal_c = np.array([2, 3, 4, 0, 0])

sal_bfs = phaseone(sal_A, sal_b)
print(sal_bfs)

salm_optm = sx.sfsimplex(sal_c, sal_A, sal_b, sal_bfs)

print(salm_optm)
# looks good, remember that the x3 = x3' + 4, so a zero value for x3' means x3 = 4
# not sure why I am getting that warning that x is not close to solution of Ax=b..?
