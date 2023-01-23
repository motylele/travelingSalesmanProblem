from os import system
from time import time
import numpy
from matplotlib import pyplot as plt
from utils.coordinatesFun import readCoordinates
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_simulated_annealing

# function to count distances
def countDistances(x, y, order):
    dist = 0.0
    order = numpy.append(order, order[0])

    for idx, item in enumerate(order):
        if idx < order.size - 1:
            dist += ((x[order[idx]] - x[order[idx + 1]])**2 + (y[order[idx]] - y[order[idx + 1]])**2)**0.5
    return dist

# function to create plot
def createPlot(nodes, solution, dist):

    x = []
    y = []
    for node in nodes:
        y.append(node[1:])
        x.append(node[:1])

    x1 = []
    y2 = []
    solution = numpy.append(solution, solution[0])

    for item in solution:
        x1.append(x[int(item)])
        y2.append(y[int(item)])
    plt.plot(x1, y2, '-ok')
    plt.suptitle("METAHEURISTIC ALGORITHM")
    plt.title("Path length = {path}".format(path=round(dist, 2)))
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()

def TSP():
    coords = readCoordinates()

    # divide coordinates into nodes
    nodes = []
    x1 = []
    y1 = []
    for item in coords:
        x = (float(item.split(",")[0][1:]))
        x1.append(float(item.split(",")[0][1:]))

        y = (float(item.split(",")[1][:-1]))
        y1.append(float(item.split(",")[1][:-1]))

        nodes.append((x, y))

    # create (n * n) distance matrix
    distance_matrix = great_circle_distance_matrix(nodes)

    # initial permutation. If not provided, it starts with a random path
    x0 = None

    # parameter used to generate new solutions
    perturbation_scheme="two_opt"

    # reduction factor (``alpha`` < 1) used to reduce the temperature
    alpha=0.9

    # maximum processing time in seconds
    max_processing_time=None

    # if not `None`, creates a log file with details about the whole execution
    log_file=None

    # if true, prints algorithm status every iteration
    verbose=False

    timeStart = time()

    # metaheuristic method
    permutation, distance = solve_tsp_simulated_annealing(
        distance_matrix,
        x0=x0,
        perturbation_scheme=perturbation_scheme,
        alpha=alpha,
        max_processing_time=max_processing_time,
        log_file=log_file,
        verbose=verbose
    )

    # dynamic method, works on small sets of data
    # permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
    timeEnd = time()

    # print results
    print("Algorithm duration = {time}".format(time=(timeEnd - timeStart)))
    print("Path of the best solution : {solution}".format(solution=permutation))
    dist = countDistances(x1, y1, permutation)
    print("Path length = {solution_fitness}".format(solution_fitness=dist))

    # plot
    createPlot(nodes, permutation, dist)

    n = input("Press any button ")
    system("cls")