"""
author: Ariel Suil Aravena [asuil]
date: 21-12-2020 (last modified on: 21-12-2020)

script to run the distance to points problem solution of Tarea 3

 == INDIVIDUAL MODEL ==
Tree composed of +, -, *, %, variable "x", and random numbers [-5, 5]

 == FITNESS ==
fitness is determined by the sum of positive distances from the function to the goal points
    fitness = - sum(dist(individual.evaluate(point_i[x]), point_i[y]))

 == GENES ==
 a gene is a Node of a Leaf on the tree
"""

from genetic_algorithm import GA
from Node import *
import random
import matplotlib.pyplot as mpl


# desired points
POINTS = [
    [3, 4],
    [6, 2],
    [7, 5]
]
# options to build solution
NODE_OPTIONS = [Div, Mult, Add, Sub]
# expected lenght of the binary representation
HEIGHT = 5
# model parameters
random.seed(528)
MUTATION_RATE = 0.8
POPULATION_SIZE = 100
GENERATIONS = 5


# calculates distance between indiviual value and desired value
# Node -> int
def fitness(individual):
    error = 0
    for point in POINTS:
        error += abs(individual.evaluate({"x": point[0]}) - point[1])
    return -error


# generates a valid gene
# int -> Node
def gene_factory(height):
    if height == 0:
        if round(random.random()):
            return Number(random.randint(-5, 5))
        return Variable("x")
    return random.choice(NODE_OPTIONS)(gene_factory(height - 1), gene_factory(height - 1))


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

# best individual
print(f"solution={best_individual.toString()}")

# plot points and function
for point in POINTS:
    mpl.plot(point[0], point[1], marker='o')

xs = []
ys = []
for x in range(100):
    xs.append(x / 10)
    ys.append(best_individual.evaluate({"x": x / 10}))

mpl.plot(xs, ys)

mpl.show()
