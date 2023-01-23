from matplotlib import pyplot as plt
from time import time
from os import system
import pygad
import numpy
from utils.coordinatesFun import readCoordinates

# function to count distances between nodes
def countDistances(x, y, order):
    dist = 0.0

    order = numpy.append(order, order[0])
    for item in zip(order, order[1:]): #list(1,2,3,4) => (1,2)(2,3)(3,4) + (4,1)
        # print(int(item[1:][0]), int(item[:-1][0]))
        dist += ((x[int(item[1:][0])] - x[int(item[:-1][0])])**2 + (y[int(item[1:][0])] - y[int(item[:-1][0])])**2)**0.5

    return -dist

# function to create plot
def createPlot(x, y, solution, solution_fitness):
    x1 = []
    y2 = []

    solution = numpy.append(solution, solution[0])

    for item in solution:
        x1.append(x[int(item)])
        y2.append(y[int(item)])
    plt.plot(x1, y2, '-ok')
    plt.suptitle("GENETIC ALGORITHM")
    plt.title("Path length = {path}".format(path=round(-solution_fitness, 2)))
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
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

    # 1) solution no 1
    gene_space = list(range(0, len(x)))

    # 2) solution no 2
    # gene_space = {'low': 0, 'high': 1}

    # number of chromosome genes, number of parameters in the function
    num_genes = len(x)

    # function to sort float values, returns permutation
    def floatOrder(floats):
        nodes = list(range(0, len(x)))
        order = list(zip(nodes, floats))  # ((0, float), (1, float), ... (n, float))
        sort = sorted(order, key=lambda a: float(a[1]))  # sorted by float values

        return list(zip(*sort))[0] # unzip: (list(order), list(float))[0]

    # fitness func -> max, return fitness value of the solution
    def fitness_func(solution, solution_idx):

        # 1) solution no 1
        return countDistances(x, y, solution)

        # 2) solution no 2
        # return countDistances(x, y, floatOrder(solution))

    fitness_function = fitness_func

    # number of chromosomes/ solutions, number of solutions in the population
    if num_genes > 10: #10 is minimum
        sol_per_pop = 50
    elif num_genes > 20:
        sol_per_pop = 80
    elif num_genes > 30:
        sol_per_pop = 100
    elif num_genes > 40:
        sol_per_pop = 150
    else:
        sol_per_pop = 200

    #number of generations
    num_generations = 200


    # number of parents to cross, number of solutions to be selected as parents in the mating pool
    # num_parents_mating = int(len(x) / 2)
    num_parents_mating = int(sol_per_pop/2) + 1


    # if 0 => no parent in the current population will be used in the next population
    # if -1 => all parents in the current population will be used in the next population
    # if > 0 => the specified value refers to the number of parents in the current population
    #                                                       to be used in the next population
    keep_parents = int(sol_per_pop * 0.01)

    # selection type => steady state selection
    parent_selection_type = "tournament"

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
    print("Algorithm duration = {time}".format(time=(timeEnd - timeStart)))
    print("Path of the best solution : {solution}".format(solution=solution))
    print("Path length = {solution_fitness}".format(solution_fitness=-solution_fitness))

    # plot generated path
    createPlot(x, y, solution, solution_fitness)

    # plot ga
    ga_instance.plot_fitness()

    n = input("Press any button ")
    system("cls")