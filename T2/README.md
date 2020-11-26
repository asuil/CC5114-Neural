# CC5114-Neural/T2
Solution to Tarea 2

## Versions Used
* Python 3.8

## Files
####genetic_algorithm.py
personal implementation of a genetic algorithm engine
####main.py
proposed solution to the N-Queen problem using the genetic algorithm engine
####binary.py
proposed solution to the finding a binary representation using the genetic algorithm engine
####word.py
proposed solution to the guessing a word using the genetic algorithm engine


## How to run
To test the solutions to the problems just run the corresponding file in the same folder as genetic_algorith.py. 

Prints on screen are turned on by default (controlled by the 'silent' variable).
While running prints will indicate the current state of the process along with the number of the current generation.
Once the algorithm ends, 
either by reaching the desired solution or the maximum number of generations, 
a plot will be displayed showing the fitness results of each generation. N-Queen (main.py) also displays a plot
showing the positions of the queens in the final solution.

The performance of the algorithm is heavily influenced by the model parameters at the start of each file. 
You can adjust mutation rate, population size and/or the number of generations there, as well as problem objectives 
(N of the N-Queen, the number to convert, and the word to guess).