"""
author: Ariel Suil Aravena [asuil]
date: 21-12-2020 (last modified on: 21-12-2020)

script to run the des chiffres et des lettres problem solution of Tarea 3

 == INDIVIDUAL MODEL ==
Tree composed of +, -, *, %, and given numbers

 == FITNESS ==
fitness is determined by the difference between the current individual evaluation and the desired number
    fitness = - abs(individual.evaluate() - desired_number)

 == GENES ==
 a gene is a Node of a Leaf on the tree
"""

from genetic_algorithm import GA
from Node import *
import random

# goal number
N = 958
# options to build solution
N_OPTIONS = [7, 3, 50, 7, 10, 6]
O_OPTIONS = [Div, Mult, Add, Sub]
# expected lenght of the binary representation
HEIGHT = 5
# model parameters
random.seed(528)
MUTATION_RATE = 0.8
POPULATION_SIZE = 500
GENERATIONS = 5


# calculates distance between indiviual value and desired value
# Node -> int
def fitness(individual):
    # return negative diference
    return - abs(N - individual.evaluate({}))


# generates a valid gene
# int -> Node
def gene_factory(height):
    if height == 0:
        return Number(random.choice(N_OPTIONS))
    return random.choice(O_OPTIONS)(gene_factory(height - 1), gene_factory(height - 1))


# generates a valid individual
# None -> Node
def individual_factory():
    return gene_factory(HEIGHT)


# build algorithm
ga = GA(pop_size=POPULATION_SIZE, mutation_rate=MUTATION_RATE, fitness=fitness,
        individual_factory=individual_factory, gene_factory=gene_factory,
        termination_condition=lambda f: f == 0, silent=False, max_iter=GENERATIONS, n_nodes=2**HEIGHT)

# run algorithm
best_fitness_list, avg_list, best_individual = ga.run()

# display results
ga.graph()

# value of best individual
print(f"value={best_individual.evaluate({})}")

# best individual
print(f"solution={best_individual.toString()}")
