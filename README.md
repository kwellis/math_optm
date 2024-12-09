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

Where $f(x)$ is the summation of the oil rate for a series of different jet pumps, represnted as $q_{oi}$. The oil rate compared to the given power fluid is represnted by an exponential function $q_{oi} = c_{1i} - c_{2i} \exp{(-q_{pi} c_{3i})}$. The coefficients are found in different numerical scheme, and vary for each pump and oil well combination.

$$f(x) = \sum_{i=1}^{n} q_{o i}$$

## Getting Started

Rawr

### Dependencies

The major dependencies required are listed below.

* Numpy
* Scipy
* Matplotlib

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```
