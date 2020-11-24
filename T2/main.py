"""
author: Ariel Suil Aravena [asuil]
date: 24-11-2020 (last modified on: 24-11-2020)

main script to run the solution of Tarea 2

chosen problem: N-Queen

 == INDIVIDUAL MODEL ==
an individual is a list of integers representing the rows and columns of each queen on a chess board
ex:
    1  2  3
 1 [X][ ][ ]
 2 [ ][ ][X]    =>      coords: (1, 1); (2, 3)      =>     [1, 1, 2, 3]
 3 [ ][ ][ ]

 == FITNESS ==
fitness is determined by how many queens are attacking each other:
    fitness = - n_of_attacks / 2
an attack is defined by having the same x-coord, same y-coord or live in the same diagonal (same sum/difference)

 == GENES ==
 a gene is simple a number between 1 and N where N is one of the dimensions of the chess board (N x N)
"""

from genetic_algorithm import GA
import matplotlib.pyplot as mpl
import random

# dimensions of chess board and number of queens
N = 30
# model parameters
random.seed(10)
MUTATION_RATE = 0.02
POPULATION_SIZE = 700
GENERATIONS = 80


# checks if 2 queens are attacking each other
# 1 if attacking, 0 else
# list(int, int), list(int, int) => int
def is_attacking(q1, q2):
    # same x
    if q1[0] == q2[0]:
        return 1
    # same y
    if q1[1] == q2[1]:
        return 1
    # same diagonal
    if q1[0] + q1[1] == q2[0] + q2[1]:
        return 1
    # same other diagonal
    if q1[0] - q1[1] == q2[0] - q2[1]:
        return 1
    # else
    return 0


# calculates how many queens are atacking each other and turns into fitness value
# list(int) -> int
def fitness(individual):

    # separate queens
    queens = [None] * N
    for j in range(N):
        queens[j] = individual[2*j:2*(j+1)]

    # calculate # of attacks
    attacks = 0
    indices = range(N)
    for this_queen in indices:
        for other_queen in indices:

            # only check on others
            if this_queen != other_queen:
                attacks += is_attacking(queens[this_queen], queens[other_queen])

    # return fitness value
    return - attacks / 2


# generates a valid gene
# None -> int
def gene_factory():
    return random.randint(1, N)


# generates a valid individual
# None -> array(int)
def individual_factory():
    return [gene_factory() for i in range(N * 2)]


# build algorithm
ga = GA(pop_size=POPULATION_SIZE, mutation_rate=MUTATION_RATE, fitness=fitness,
        individual_factory=individual_factory, gene_factory=gene_factory,
        termination_condition=lambda f: f == 0, silent=False, max_iter=GENERATIONS)

# run algorithm
best_fitness_list, avg_list, best_individual = ga.run()

# display results
ga.graph()

# separate queens on best individual
queen_list = [None] * N
for i in range(N):
    q = best_individual[2*i:2*(i+1)]
    queen_list[i] = q

# plot queens to visualize solution
for queen in queen_list:
    mpl.plot(queen[0], queen[1], marker='o')
mpl.show()
