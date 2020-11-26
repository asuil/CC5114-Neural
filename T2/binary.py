"""
author: Ariel Suil Aravena [asuil]
date: 24-11-2020 (last modified on: 26-11-2020)

script to run the binary problem solution of Tarea 2

 == INDIVIDUAL MODEL ==
an individual is a list of integers (0, 1) in the reverse order of the binary number
ex:
 001010     =>      [0, 1, 0, 1, 0, 0]

 == FITNESS ==
fitness is determined by the difference of the current individual turned into decimal and the number we want
    fitness = - abs(NUMBER_TO_CONVERT - sum)

 == GENES ==
 a gene is simple a 0 or a 1
"""

from genetic_algorithm import GA
import random

# goal number
N = 2068
# expected lenght of the binary representation
N_LENGHT = 20
# model parameters
random.seed(0)
MUTATION_RATE = 0.2
POPULATION_SIZE = 150
GENERATIONS = 20


# returns value of reversed binary representation
# list(10*int) => int
def value(individual):

    # calculate indivual's value
    result = 0
    for i in range(len(individual)):
        result += individual[i] * (2 ** i)

    return result


# calculates distance between indiviual value and desired value
# list(int) -> int
def fitness(individual):
    # return negative diference
    return - abs(N - value(individual))


# generates a valid gene
# None -> int
def gene_factory():
    return random.randint(0, 1)


# generates a valid individual
# None -> array(int)
def individual_factory():
    return [gene_factory() for dummy in range(N_LENGHT)]


# build algorithm
ga = GA(pop_size=POPULATION_SIZE, mutation_rate=MUTATION_RATE, fitness=fitness,
        individual_factory=individual_factory, gene_factory=gene_factory,
        termination_condition=lambda f: f == 0, silent=False, max_iter=GENERATIONS)

# run algorithm
best_fitness_list, avg_list, best_individual = ga.run()

# display results
ga.graph()

# value of best individual
print(f"value={value(best_individual)}")

# best individual
best_individual.reverse()
print(f"representation={best_individual}")
