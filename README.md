# Optimization Fall 2024 Class Code

The following is a collection of code written for assignments for a semester long class in optimization at UAF. The class was taught in the math department by Ed Bueler. The code was not updated after grading, so use at your own risk if you are taking the class during a different semester. The class culiminated in a class project, which is inside a folder called capstone.

## Capstone Class Project

For the class project, a reduced Newton method with active set constraints was applied. The project was an optimization scheme for properly allocating power fluid to jet pump assisted wells. The problem takes the form:

$$
\begin{matrix} 
\min & f(x) \\\\ 
\text{subject to} & A x \geq b  \\\\ 
& x \ge 0 
\end{matrix}
$$

Where $f(x)$ is the summation of the negative oil rate for a series of different jet pumps, represnted as $q_{oi}$. The oil rate compared to the given power fluid, $q_{pi}$ is represnted by an exponential function $q_{oi} = - c_{1i} + c_{2i} \exp{(-q_{pi} c_{3i})}$. The coefficients are found in different numerical scheme, and vary for each pump and oil well combination. It will be noted, that $q_{oi}$ is a negative number, to turn the maximization problem to minimization. The vector $x$ represents the individual power fluid rates to each well $x=(q_{pi}, q_{p2}, ..., q_{pn})^{T}$.

$$f(x) = \sum_{i=1}^{n} q_{o i}$$

Each well is required to have a non-zero minimum power fluid rate, represented as $q_{pi} \geq 0$. This will create $n$ constraints. Additionally, the summed power fluid of each well needs to be lower than the power fluid from a surface supply pump, represented as $Q_p^{tot}$. This adds another constraint, bringing the total constraints to $n+1$. The constraint for the total power fluid is shown below.

$$\sum_{i=1}^{n} q_{p i} \leq Q_p^{tot}$$

### Dependencies

The only significant dependency in the code is numpy, which is used for its array and linear algebra support.

## Getting Started

The file to call is under the folder capstone, file assemply. The main function is optimize power fluid. Which requires a dictionary that defines the well coefficient properties and a total available power fluid called qp_tot. An example of what is required to define is shown below.

```python
from capstone.assembly import optimize_power_fluid

wells = {
  "well_1": {"c1": 353, "c2": 230, "c3": 9.6e-4, "qp_min": 0},
  "well_2": {"c1": 578, "c2": 430, "c3": 5.6e-4, "qp_min": 0},
  "well_3": {"c1": 1237, "c2": 1226, "c3": 7.35e-4, "qp_min": 0},
  "well_4": {"c1": 944, "c2": 807, "c3": 6.9e-4, "qp_min": 0},
    }

Qp_tot = 12500  # max available water flow in the system
Qo, Qp, dfk, k = optimize_power_fluid(wells, Qp_tot)
```
The function will return the estimated total amount of the oil produced, the distribution of power fluid to each well, the gradient of each well and the required number of iterations to converge to an answer.

Any desired number of wells can be added onto the dictionary and used to help evenly distribute the power fluid among the different available jet pumped wells.
