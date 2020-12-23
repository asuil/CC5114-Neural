# CC5114-Neural/T3
Solution to Tarea 3

## Versions Used
* Python 3.8

## Files
#### genetic_algorithm.py
personal implementation of a genetic programming engine (modified from T2)
#### desChiffresEtDesLettres.py
proposed solution to the des chiffres et des lettres problem using the genetic programming engine
#### functionPoints.py
proposed solution to the finding a function that approximates points using the genetic programming engine
#### Node.py
library to manipulate program trees 


## How to run
To test the solutions to the problems just run the corresponding file in the same folder as genetic_algorith.py and Node.py. 

Prints on screen are turned on by default (controlled by the 'silent' variable).
While running prints will indicate the current state of the process along with the number of the current generation.
Once the algorithm ends, 
either by reaching the desired solution or the maximum number of generations, 
a plot will be displayed showing the fitness results of each generation. functionPoints.py also displays a plot
showing the initial points and result function.

The performance of the algorithm is heavily influenced by the model parameters at the start of each file. 
You can adjust mutation rate, population size and/or the number of generations there, as well as problem objectives 
(N and operations for dcedl, and points for functionPoints).
