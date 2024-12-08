# bring it all together

import time
import timeit

import network as nw
import numpy as np
import ratio_test as rt


def optimize_power_fluid(well_dict: dict, Qp_tot: float) -> tuple[float, np.ndarray, np.ndarray, int]:
    """Optimize Power Fluid

    Args:
        well_dict (dict): Well Dictionary of Definied Parameters
        Qp_tot (float): Total Available Power Fluid to Split out

    Return:
        Qo (float): Maximized Oil Rate for the wells
        Qp (np.array): Array of gradients for each well
        dfk (np.array): Gradient at each well
        k (int): Number of Iterations
    """
    Qp = nw.guess_Qp(well_dict, Qp_tot)
    A, b = nw.constraint_spaces(well_dict, Qp_tot)
    # print(f"Matrix A:\n{A}\n")
    # print(f"Vector b:\n{b}\n")
    active = nw.constraint_active(A, b, Qp)  # active constraints
    # print(f"Active Constraints:\n{active}\n")
    Z, Ar = nw.qr_split(A[active])
    # print(f"Null Space:\n{Z}\n")
    # print(f"Right Inverse:\n{Ar}\n")

    dfk = nw.update_gradient(well_dict, Qp)
    # hfk = nw.update_hessian(well_dict, Qp)
    # print(f"Gradient:\n{dfk}\nHessian:\n{hfk}\n")

    optm_check, active, con_update = nw.optimality_test(dfk, Z, Ar, active)
    if con_update:  # active constraint was removed, need to update
        Z, Ar = nw.qr_split(A[active])

    k = 0
    while optm_check is False:

        dfk = nw.update_gradient(well_dict, Qp)
        Hfk = nw.update_hessian(well_dict, Qp)

        optm_check, active, con_update = nw.optimality_test(dfk, Z, Ar, active)
        if con_update:  # active constraint was removed
            Z, Ar = nw.qr_split(A[active])  # update Z and Ar

        p = nw.newton_reduced(dfk, Hfk, Z)

        alpha = nw.line_search_backtrack(nw.update_objective, well_dict, Qp, dfk, p)
        tau, idx = rt.ratio_test(Qp, p, A[~active], b[~active], np.where(~active)[0])  # distance to constraints

        if tau <= alpha:
            alpha = tau
            active[idx] = True  # active constraint added
            Z, Ar = nw.qr_split(A[active])  # update Z and Ar

        Qp = Qp + alpha * p

        if k == 100:
            break
        k = k + 1

    return nw.update_objective(well_dict, Qp), Qp, dfk, k


if __name__ == "__main__":
    # define the wells and define the minimum power fluid flowrate in BPD
    wells = {
        "india_15": {"c1": 353, "c2": 230, "c3": 9.6e-4, "qp_min": 0},
        "india_17": {"c1": 578, "c2": 430, "c3": 5.6e-4, "qp_min": 0},
        "india_33": {"c1": 1237, "c2": 1226, "c3": 7.35e-4, "qp_min": 0},
        "india_31": {"c1": 944, "c2": 807, "c3": 6.9e-4, "qp_min": 0},
    }

    Qp_tot = 12500  # max available water flow in the system

    t0 = time.time()
    Qo, Qp, dfk, k = optimize_power_fluid(wells, Qp_tot)
    t1 = time.time()

    dur = timeit.timeit(lambda: optimize_power_fluid(wells, Qp_tot), number=10)

    print(f"\nRequired Iterations: {k}")
    print(f"Total Oil Rate: {-1*Qo :.2f}")
    print(f"Distributed Power Fluid:\n{Qp}")
    print(f"Gradient at each well:\n{dfk}")
    print(f"Sum Individual Power Fluid: {sum(Qp):.2f}")
    print(f"Took: {dur}")
