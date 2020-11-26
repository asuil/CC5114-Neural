"""
author: Ariel Suil Aravena [asuil]
date: 26-11-2020 (last modified on: 26-11-2020)

script to run the word problem solution of Tarea 2

 == INDIVIDUAL MODEL ==
an individual is a list of characters in the order of the word
ex:
 cat     =>      ['c', 'a', 't']

 == FITNESS ==
fitness is determined by how many characters are right
    fitness = good_characters
the number of good characters is determined just by counting

 == GENES ==
 a gene is simple a random lowercase letter
"""

from genetic_algorithm import GA
import random
import string

# goal word
W = "estornudo"
# lenght of word
L = len(W)
# model parameters
random.seed(1)
MUTATION_RATE = 0.3
POPULATION_SIZE = 200
GENERATIONS = 30


# calculates difference between and individual and the goal word
# list(char) -> int
def fitness(individual):
    rights = 0
    for i in range(len(individual)):
        rights += (individual[i] == W[i])
    return rights


# generates a valid gene
# None -> int
def gene_factory():
    return random.choice(string.ascii_lowercase)


# generates a valid individual
# None -> array(int)
def individual_factory():
    return [gene_factory() for dummy in range(L)]


# build algorithm
ga = GA(pop_size=POPULATION_SIZE, mutation_rate=MUTATION_RATE, fitness=fitness,
        individual_factory=individual_factory, gene_factory=gene_factory,
        termination_condition=lambda f: f == L, silent=False, max_iter=GENERATIONS)

# run algorithm
best_fitness_list, avg_list, best_individual = ga.run()

# display results
ga.graph()

# best individual
print(f"guessed word={''.join(best_individual)}")
