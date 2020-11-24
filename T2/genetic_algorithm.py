"""
author: Ariel Suil Aravena [asuil]
date: 24-11-2020 (last modified on: 24-11-2020)

genetic algorithm implementation

"""


# class that represents a genetic algorithm and allows to run it
# pop_size:                 (int) Number of individuals per generation
# mutation_rate:            (float) Percentage of mutation of individual ]0, 1[
# fitness:                  (array(gene*) -> float) Function that evaluates fitness of an individual
# individual_factory:       (None -> array(genes*)) Function that creates individuals
# gene_factory:             (None -> gene*) Function that creates a gene (section of an individual)
# termination_condition:    (float -> bool) Functions that recieves the fitness of an individual and returns whether the algorithm should end or not
# silent:                   (bool) Turns on/off algorithm prints
# max_iter:                 (int) Maximum number of iterations before ending the algorithm [>0 or -1 to disable]
#
# a 'gene' could be any object as long as it's the same in all given functions
class GA:

    # constructor
    def __init__(self, pop_size, mutation_rate, fitness, individual_factory,
                 gene_factory, termination_condition, silent, max_iter):

        self.__gene = type(gene_factory())
        if not silent:
            print(f"Type of genes: {self.__gene}")

        self.__pop_size = pop_size
        self.__mut_rate = mutation_rate
        self.__fitness = fitness
        self.__i_factory = individual_factory
        self.__g_factory = gene_factory
        self.__end_cond = termination_condition
        self.__silent = silent
        self.__max_iter = max_iter

    # execute algorithm, returns best individual
    # None -> array(gene)
    def run(self):

        if not self.__silent:
            print("Starting Algorithm")

        # INITIALIZE POPULATION
        individuals = [self.__i_factory() for i in range(self.__pop_size)]

        iterations = 0
        best_fitness_list = [None] * self.__max_iter
        avg_fitness_list = [None] * self.__max_iter
        while iterations != self.__max_iter:

            if not self.__silent:
                print(f"Generation {iterations} started fitness evaluation")

            # EVALUATE FITNESS
            fitness_results = [self.__fitness(individual) for individual in individuals]

            if not self.__silent:
                print("Recording fitness data")

            # RECORD DATA
            best_fitness = max(fitness_results)
            avg_fitness = sum(fitness_results) / len(fitness_results)
            best_fitness_list[iterations] = best_fitness
            avg_fitness_list[iterations] = avg_fitness

            if not self.__silent:
                print("Finding best individual")

            # OBTAIN BEST
            best_index = fitness_results.index(best_fitness)
            best_individual = individuals[best_index]

            if not self.__silent:
                print(f"Best individual found: {best_individual}")

            # TEST IF DONE
            iterations += 1
            if self.__end_cond(best_fitness):
                if not self.__silent:
                    print("Best individual fits termination condition")
                break

            if not self.__silent:
                print("Selecting parents from individuals")
            # SELECTION (tournament)

            if not self.__silent:
                print(f"Mutating parents to create new generation")
            # MUTATION

        if not self.__silent:
            print("Algorithm Finished")
            print(f"Number of generations: {iterations}")

        return best_fitness_list, avg_fitness_list, best_individual
