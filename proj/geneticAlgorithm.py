from matplotlib import pyplot as plt
from os import system
import pygad
import numpy


def countDistances(x, y, order):
    dist = 0.0

    # for idx, item in enumerate(x):
    #     if idx != len(x) - 1:
    #         dist += ((x[idx] - x[idx + 1])**2 + (y[idx] - y[idx + 1])**2)**0.5
    # return dist
    order = numpy.append(order, order[0])
    for item in zip(order, order[1:]): #list(1,2,3,4) => (1,2)(2,3)(3,4) + (4,1)
        # print(int(item[1:][0]), int(item[:-1][0]))
        dist += ((x[int(item[1:][0])] - x[int(item[:-1][0])])**2 + (y[int(item[1:][0])] - y[int(item[:-1][0])])**2)**0.5

    return -dist


def createPlot(x, y, solution):
    x1 = []
    y2 = []

    solution = numpy.append(solution, solution[0])

    for item in solution:
        x1.append(x[int(item)])
        y2.append(y[int(item)])
    plt.plot(x1, y2, '-ok')
    plt.show()

def geneticAlgorithm():
    coords = []
    with open("\INF-D-2023-Mateusz-Motyl-269381\\utils\cords.txt", "r") as f:
        for line in f:
            coords.append(line.rstrip('\n'))
    f.close()

    #split coordinates into x & y
    x = []
    y = []
    for item in coords:
        x.append(float(item.split(",")[0][1:]))
        y.append(float(item.split(",")[1][:-1]))

    #list(0, 1, ..., len(x))
    gene_space = list(range(0, len(x)))

    #num of chromosome genes
    num_genes = len(x)

    #fitness func -> max
    def fitness_func(solution, solution_idx):
        # print(solution)
        return countDistances(x, y, solution)
    fitness_function = fitness_func

    #num of chromosomes/ solutions
    if len(x) > 10: #10 is minimum
        sol_per_pop = 50
    elif len(x) > 20:
        sol_per_pop = 70
    elif len(x) > 30:
        sol_per_pop = 100
    elif len(x) > 40:
        sol_per_pop = 150
    else:
        sol_per_pop = 200

    #num of parents to cross
    num_parents_mating = int(len(x) / 2)
    # num_parents_mating = int(sol_per_pop/2) + 1 #??

    #num of generations
    num_generations = 50


    keep_parents = int(sol_per_pop * 0.05)

    #selection type => steady state selection
    parent_selection_type = "sss"

    #crossover type => single point
    crossover_type = "single_point"

    #mutation type => random
    mutation_type = "random"

    #mutation percent
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

    #run pygad
    ga_instance.run()

    #best solution & valued
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Ścieżka najlepszego rozwiązania : {solution}".format(solution=solution))
    print("Długość = {solution_fitness}".format(solution_fitness=-solution_fitness))

    #plot generating
    createPlot(x, y, solution)

    #end
    n = input("Naciśnij klawisz, żeby powrócić ")
    system("cls")