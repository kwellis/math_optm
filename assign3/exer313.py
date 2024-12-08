import numpy as np


def check_array_length(*arrays):
    lengths = [len(arr) for arr in arrays]
    if len(set(lengths)) != 1:
        raise ValueError("All numpy arrays must have the same length. Got lengths: {}".format(lengths))


def feasible_point(x_vec: np.ndarray, a_mat: np.ndarray, b_vec: np.ndarray) -> None:
    """Feasible Point

    Verify whether the x_vector is actually inside the feasible set or not.
    The inequalities have to take the form Ax >= b.

    Args:
        x_vec (np.ndarray): Vector of Feasible Points
        p_vec (np.ndarray): Vector of Feasible Directions
        a_mat (np.ndarray): Matrix of Constraint Gradients
        b_vec (float): Vector of Constraint Locations

    Return:
        None
    """
    for a_vec, b_sca in zip(a_mat, b_vec):
        if a_vec @ x_vec.T < b_sca:
            raise ValueError(f"The point {x_vec} not feasible with ai:{a_vec} and bi: {b_sca}")
    return None


def feasible_angle(p_vec: np.ndarray, a_vec: np.ndarray) -> float:
    """Feasible Angle

    Args:
        p_vec (np.ndarray): Vector of Feasible Directions
        a_vec (np.ndarray): Vector of Constraint Gradients

    Return:
        angle: (float): Angle between feasible direction and gradients
                less than 0 is towards, greater than 0 is away, zero is orthogo
    """
    check_array_length(p_vec, a_vec)

    angle = a_vec.T @ p_vec
    return float(angle)  # grab the first value, should be a scalar


def feasible_dist(x_vec: np.ndarray, a_vec: np.ndarray, b_sca: float) -> float:
    """Feasible Distance

    Args:
        x_vec (np.ndarray): Vector of Feasible Points
        a_vec (np.ndarray): Vector of Constraint Gradients
        b_sca (float): Scalar Representing Constraint Location

    Return:
        dist: (float): Distance Feasible Point is from Boundary
    """
    check_array_length(x_vec, a_vec)

    dist = a_vec.T @ x_vec - b_sca
    return float(dist)


def max_step_size(x_vec: np.ndarray, p_vec: np.ndarray, a_mat: np.ndarray, b_vec: np.ndarray) -> float:
    """Calculate the max step size

    Args:
        x_vec (np.ndarray): Vector of Feasible Points
        p_vec (np.ndarray): Vector of Feasible Directions
        a_mat (np.ndarray): Matrix of Constraint Gradients
        b_vec (float): Vector of Constraint Locations

    Return:
        alpha: (float): Distance Point can move
    """
    # check all the points are feasible first
    feasible_point(x_vec, a_mat, b_vec)
    step_sizes = []  # list to store the various step sizes
    # loop through the a matrix and the b vector
    for a_vec, b_sca in zip(a_mat, b_vec):
        fdist = feasible_dist(x_vec, a_vec, b_sca)
        fangl = feasible_angle(p_vec, a_vec)
        if fangl >= 0:
            step_size = np.inf
        else:
            step_size = fdist / (-1 * fangl)
        step_sizes.append(step_size)
    print(step_sizes)
    return np.nanmin(step_sizes)  # return minimum step size


if __name__ == "__main__":
    print("Testing the Code with Example 3.4 from the Book")
    # test code with example 3.4
    a_mat = np.array([[1, 4], [0, 3], [5, 1]])
    b_vec = np.array([3, 2, 4])
    xe = np.array([1, 1])
    pe = np.array([4, -2])

    alpha_e = max_step_size(xe, pe, a_mat, b_vec)
    print(alpha_e)

    print("\nRunning Code on Constraints from Exercise 3.1.3")
    a_mat = np.array([[9, 4, 1, 9, -7], [6, -7, 8, -4, -6], [1, 6, 3, -7, 6]])
    b_vec = np.array([-15, -30, -20])

    print("Part i")
    xa = np.array([8, 4, -3, 4, 1])
    pa = np.array([1, 1, 1, 1, 1])
    alpha_a = max_step_size(xa, pa, a_mat, b_vec)
    print(alpha_a)

    print("Part ii")
    xb = np.array([7, -4, -3, -3, 3])
    pb = np.array([3, 2, 0, 1, -2])
    alpha_b = max_step_size(xb, pb, a_mat, b_vec)
    print(alpha_b)

    print("Part iii")
    xc = np.array([5, 0, -6, -8, -3])
    pc = np.array([5, 0, 5, 1, 3])
    alpha_c = max_step_size(xc, pc, a_mat, b_vec)
    print(alpha_c)

    print("Part iv")
    xd = np.array([9, 1, -1, 6, 3])
    pd = np.array([-4, -2, 4, -2, 2])
    alpha_d = max_step_size(xd, pd, a_mat, b_vec)
    print(alpha_d)

    # the other method is calculate two vectors, ai.T*p and ai.T*x, with those,
