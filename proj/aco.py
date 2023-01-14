from utils.coordinatesFun import readCoordinates
from matplotlib import pyplot as plt
from os import system
import pants

def countDistances(x, y):
    return ((x[1] - y[1])**2 + (x[0] - y[0])**2)**0.5

def createPlot(path):
    x = []
    y = []

    tour = path.tour
    tour.append(tour[0])
    for item in tour:
        y.append(item[1:])
        x.append(item[:1])

    plt.plot(x, y, '-ok')
    plt.suptitle("ALGORYTM ACO")
    plt.title("Długość ścieżki = {path}".format(path=round(path.distance, 2)))
    plt.xlabel("Szerokość geograficzna")
    plt.ylabel("Długość geograficzna")
    plt.show()

def ACO():
    coords = readCoordinates()

    # divide coordinates into nodes
    nodes = []
    for item in coords:
        x = (float(item.split(",")[0][1:]))
        y = (float(item.split(",")[1][:-1]))
        nodes.append((x, y))


    # [World] is created from a list of nodes & length function (+ optionally name and description)
    world = pants.World(nodes, countDistances)

    # [float] relative importance of pheromone (default=1)
    alpha = 1

    # [float] relative importance of distance (default=3)
    beta = 3

    # [float] percent evaporation of pheromone (0..1, default=0.8)
    rho = 0.8

    # [float] total pheromone deposited by each ant (>0, default=1)
    q = 1

    # [float] initial pheromone level along each edge of world (>0, default=0.01)
    t0 = .01

    # [int] number of iterations to perform (default=100)
    limit = 100

    # [float] how many ants will be used (default=10)
    ant_count = 10

    # [float] multiplier of the pheromone deposited by the elite ant (default=0.5)
    elite = .5

    # for best results
    # 0.5 <= alpha <= 1
    # 1.0 <= beta <= 5
    # alpha < beta
    # limit >= 2000
    # ant count > 1

    solver = pants.Solver(
        alpha=alpha,
        beta=beta,
        rho=rho,
        q=q,
        t0=t0,
        limit=limit,
        ant_count=ant_count,
        elite=elite
    )

    # return the shortest path found through the given [World]
    # param: the [World] to solve
    # return: best solution found
    # rtype: [Ant]
    solution = solver.solve(world)


    print(solution.distance)
    createPlot(solution)

    n = input("Naciśnij klawisz, żeby powrócić ")
    system("cls")