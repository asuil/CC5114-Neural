# CC5114-Neural/T2
Solution to Tarea 2

## Versions Used
* Python 3.8

## Files
####binary_example.py
working example on how to use a genetic algorithm (given in class)
####genetic_algorithm.py
personal implementation of a genetic algorithm engine
####main.py
proposed solution to the N-Queen problem using the genetic algorithm engine

## How to run
To test the solution to the N-Queen problem run the main.py file in the same folder as genetic_algorith.py. 

Prints on screen are turned on by default (controlled by the 'silent' variable).
While running prints will indicate the current state of the process along with the number of the current generation.
Once the algorithm ends, 
either by reaching the desired solution or the maximum number of generations, 
two plots will be displayed: 
one showing the fitness results of each generation and another showing the positions of the queens in the final solution.

The performance of the algorithm is heavily influenced by the model parameters at the start of the main.py file. 
You can adjust mutation rate, population size and/or the number of generations there.