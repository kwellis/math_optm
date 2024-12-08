# Optimization Fall 2024 Class Code

The following is a collection of code written for assignments for a semester long class in optimization at UAF. The class was taught in the math department by Ed Bueler. The code was not updated after grading, so use at your own risk if you are taking the class during a different semester. The class culiminated in a class project, which is inside a folder called capstone.

## Capstone Class Project

For the class project, a reduced Newton method with active set constraints was applied. The project was an optimization scheme for properly allocating power fluid to jet pump assisted wells. The problem takes the form:

maximize \( f(x) = \sum_{i=1}^{n} q_{o\:i} \)

subject to:

- \( \sum_{i=1}^{n} q_{p\:i} \leq Q_{\text{p}}^{\text{tot}} \)
- \( q_{p\:i} \geq 0 \)


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
