from matplotlib import pyplot as plt
from time import time
from os import system
import pygad
import numpy

from utils.coordinatesFun import readCoordinates


def countDistances(x, y, order):
    dist = 0.0

    order = numpy.append(order, order[0])
    for item in zip(order, order[1:]): #list(1,2,3,4) => (1,2)(2,3)(3,4) + (4,1)
        # print(int(item[1:][0]), int(item[:-1][0]))
        dist += ((x[int(item[1:][0])] - x[int(item[:-1][0])])**2 + (y[int(item[1:][0])] - y[int(item[:-1][0])])**2)**0.5

    return -dist


def createPlot(x, y, solution, solution_fitness):
    x1 = []
    y2 = []

    solution = numpy.append(solution, solution[0])

    for item in solution:
        x1.append(x[int(item)])
        y2.append(y[int(item)])
    plt.plot(x1, y2, '-ok')
    plt.suptitle("ALGORYTM GENETYCZNY")
    plt.title("Długość ścieżki = {path}".format(path=round(-solution_fitness, 2)))
    plt.xlabel("Szerokość geograficzna")
    plt.ylabel("Długość geograficzna")
    plt.show()

def geneticAlgorithm():
    coords = readCoordinates()

    # split coordinates into x & y
    x = []
    y = []
    for item in coords:
        x.append(float(item.split(",")[0][1:]))
        y.append(float(item.split(",")[1][:-1]))

    # list(0, 1, ..., len(x)), list of all possible values of the gene
    gene_space = list(range(0, len(x)))

    # number of chromosome genes, number of parameters in the function
    num_genes = len(x)

    # fitness func -> max, return fitness value of the solution
    def fitness_func(solution, solution_idx):
        # print(solution)
        return countDistances(x, y, solution)
    fitness_function = fitness_func

    # number of chromosomes/ solutions, number of solutions in the population
    if len(x) > 10: #10 is minimum
        sol_per_pop = 50
    elif len(x) > 20:
        sol_per_pop = 80
    elif len(x) > 30:
        sol_per_pop = 100
    elif len(x) > 40:
        sol_per_pop = 150
    else:
        sol_per_pop = 200

    # number of parents to cross, number of solutions to be selected as parents in the mating pool
    num_parents_mating = int(len(x) / 2)
    # num_parents_mating = int(sol_per_pop/2) + 1 #??

    #number of generations
    num_generations = 50

    # if 0 => no parent in the current population will be used in the next population
    # if -1 => all parents in the current population will be used in the next population
    # if > 0 => the specified value refers to the number of parents in the current population
    #                                                       to be used in the next population
    keep_parents = int(sol_per_pop * 0.01)

    # selection type => steady state selection
    parent_selection_type = "sss"

    # crossover type => single point
    # if None => step bypassed
    crossover_type = "single_point"

    # mutation type => random
    # if None => step bypassed
    mutation_type = "random"

    # mutation percent, default=10%
    # no action if mutation_probability or mutation_num_genes exist
    mutation_percent_genes = int((1 / len(x)) * 100) + 1

    ga_instance = pygad.GA(
                           gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           allow_duplicate_genes=False,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)

    # run pygad & time measure
    timeStart = time()
    ga_instance.run()
    timeEnd = time()

    # best solution & valued & time
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Czas trwania algorytmu = {time}".format(time=(timeEnd - timeStart)))
    print("Ścieżka najlepszego rozwiązania : {solution}".format(solution=solution))
    print("Długość = {solution_fitness}".format(solution_fitness=-solution_fitness))

    # plot generated path
    createPlot(x, y, solution, solution_fitness)

    # plot ga
    ga_instance.plot_fitness()

    n = input("Naciśnij klawisz, żeby powrócić ")
    system("cls")