"""
author: Ariel Suil Aravena [asuil]
date: 24-11-2020 (last modified on: 21-12-2020)

genetic algorithm implementation
[modified to work with program trees for Tarea 3]
"""

import math
import random
import matplotlib.pyplot as mpl


# class that represents a genetic algorithm and allows to run it
# pop_size:                 (int) Number of individuals per generation
# mutation_rate:            (float) Percentage of mutation of individual ]0, 1[
# fitness:                  (array(gene*) -> float) Function that evaluates fitness of an individual
# individual_factory:       (None -> Node) Function that creates individuals
# gene_factory:             (None -> Node/Leaf) Function that creates a gene (section of an individual)
# termination_condition:    (float -> bool) Functions that recieves the fitness of an individual and returns whether the algorithm should end or not
# silent:                   (bool) Turns on/off algorithm prints
# max_iter:                 (int) Maximum number of iterations before ending the algorithm [>0 or -1 to disable]
#
# run()     executes algorithm
# graph()   displays results of fitness function
#
# individuals are trees, genes are its nodes and leaves
class GA:

    # constructor
    def __init__(self, pop_size, mutation_rate, fitness, individual_factory,
                 gene_factory, termination_condition, silent, max_iter, n_nodes):

        self.__pop_size = pop_size
        self.__mut_rate = mutation_rate
        self.__n_nodes = n_nodes
        self.__fitness = fitness
        self.__i_factory = individual_factory
        self.__g_factory = gene_factory
        self.__end_cond = termination_condition
        self.__silent = silent
        self.__max_iter = max_iter

        # space to save results to graph later
        self.__last_best_results = []
        self.__last_avg_results = []

    # execute algorithm, returns best individual
    # None -> array(gene)
    def run(self):

        if not self.__silent:
            print("Starting Algorithm")

        # INITIALIZE POPULATION
        individuals = [self.__i_factory() for i in range(self.__pop_size)]

        iterations = 0
        best_fitness_list = []
        avg_fitness_list = []
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
            best_fitness_list.append(best_fitness)
            avg_fitness_list.append(avg_fitness)

            if not self.__silent:
                print("Finding best individual")

            # OBTAIN BEST
            best_index = fitness_results.index(best_fitness)
            best_individual = individuals[best_index]

            if not self.__silent:
                print(f"Best individual found: {best_individual.toString()}")

            # TEST IF DONE
            iterations += 1
            if self.__end_cond(best_fitness):
                if not self.__silent:
                    print("Best individual fits termination condition")
                break

            if not self.__silent:
                print("Selecting parents from individuals")

            # SELECTION (tournament)
            # since we're crossovering every parent with each other once, we'll get (parents-1)^2 children
            # taking the inverse, we need sqrt(pop_size)+1 parents to fill the pop_size
            n_parents = math.ceil(math.sqrt(self.__pop_size) + 1)
            parents = [None] * n_parents
            for i in range(n_parents):

                # we take a population sample relative to the number of parents
                # 1/n_parents was chosen since it means giving a chance to pretty much anyone to be chosen as a parent
                fitness_sample = random.sample(fitness_results, int(self.__pop_size * (1 / n_parents)))

                # we get the best one
                best_local_index = fitness_results.index(max(fitness_sample))
                best_local_individual = individuals[best_local_index]

                # we save the best as a parent
                parents[i] = best_local_individual  # save individual instead of index for code readability

            if not self.__silent:
                print("Crossovering parents to create new generation")

            # CROSSOVER
            children = [None] * (n_parents * (n_parents-1))
            child_index = 0
            for i_parent in range(n_parents):
                for other_parent in range(n_parents):

                    # don't crossover with self
                    if i_parent != other_parent:
                        child = crossover(parents[i_parent], parents[other_parent], self.__n_nodes, self.__mut_rate)
                        children[child_index] = child
                        child_index += 1

            if not self.__silent:
                print("Mutating children of new generation")

            # MUTATION
            children = [mutate(child, self.__g_factory, self.__n_nodes, self.__mut_rate) for child in children]

            if not self.__silent:
                print("Setting new generation as population")

            # RE-DEFINE POPULATION
            individuals = random.sample(children, self.__pop_size)  # reduce children to population size

        if not self.__silent:
            print("Algorithm Finished")
            print(f"Number of generations: {iterations}")

        # SAVE RESULTS TO GRAPH
        self.__last_best_results = best_fitness_list
        self.__last_avg_results = avg_fitness_list

        return best_fitness_list, avg_fitness_list, best_individual

    # displays graph showing fitness function results
    # None -> None
    def graph(self):
        x = range(1, len(self.__last_best_results) + 1)
        y1 = self.__last_best_results
        y2 = self.__last_avg_results
        mpl.plot(x, y1, marker='o')
        mpl.plot(x, y2, marker='o')
        mpl.legend(['best fitness', 'average fitness'])
        mpl.xlabel('number of generation')
        mpl.ylabel('fitness function result')
        mpl.show()


# simulates crossover of individuals using two parents (p1, p2) and the number of genes to change (nmut)
# Node, Node, int, float -> Node
def crossover(p1, p2, n_nodes, mut_rate):

    # create index using mut_rate + noise
    index = math.floor((1 - mut_rate) * n_nodes)
    noise = random.randint(0, math.floor(n_nodes / 10))

    # format index
    bin_index = bin(index + noise)[2:]

    # replace sub-node from p2 into p1
    child = p1.copy()
    new_branch = p2.subcopy(bin_index)
    child.replace(bin_index, new_branch)
    return child


# simulates mutation of genes replacing nmut genes of individual (i) using the factory (g_fact)
# array(gene), int -> array(gene)
def mutate(i, g_fact, n_nodes, mut_rate):

    # create index using mut_rate + noise
    index = math.floor((1 - mut_rate) * n_nodes)
    noise = random.randint(0, math.floor(n_nodes / 10))
    node_index = index + noise

    # format index
    bin_index = bin(node_index)[2:]

    # we take rounded height of sub-tree
    tree_height = math.log(n_nodes, 2)
    node_height = math.log(node_index, 2)
    child_height = round(tree_height - node_height)

    # create new node
    child = g_fact(child_height)

    # new individual
    new_i = i.copy()
    new_i.replace(bin_index, child)
    return new_i
