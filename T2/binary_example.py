# example provided to test genetic algorithms

from genetic_algorithm import GA
import random

NUMBER_TO_CONVERT = 121
NUMBER_OF_GENES = 10


def fitness_bits(anIndividual):
    result = 0
    exp = 1
    for v in anIndividual[::-1]:
        result += int(v) * exp
        exp *= 2
    return - abs(NUMBER_TO_CONVERT - result)


def gene_factory():
    if(random.random() > 0.5):
        return '1'
    else:
        return '0'


def sequence_bit_factory():
    return [gene_factory() for i in range(NUMBER_OF_GENES)]

ga = GA(pop_size=100,mutation_rate=0.1,fitness=fitness_bits,
 individual_factory=sequence_bit_factory, gene_factory=gene_factory,
 termination_condition = lambda f : f == 0, silent = False, max_iter=10)

best_fitness_list, avg_list, best_individual = ga.run()

print(''.join(best_individual))
