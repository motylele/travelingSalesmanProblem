from proj.aco import ACO
from proj.geneticAlgorithm import geneticAlgorithm
from proj.tsp import TSP
from utils.coordinatesFun import generateCoordinates, printCoordinates

while 1:
    print("Mateusz Motyl")
    print("Inf. Dz. II st.")
    print("ind: 269381\n\n")

    print("Traveling salesman problem")
    print("Variants selection:")
    print("1 - generate new coordinates")
    print("2 - show generated coordinates")
    print("3 - genetic algorithm")
    print("4 - ant colony optimization")
    print("5 - metaheuristic method")
    print("_ - end")

    x = input("Variants selection: ")
    if x.isnumeric():
        x = int(x)
        if x == 1:
            n = int(input("Enter the number of nodes: "))
            generateCoordinates(n)
        elif x == 2:
            printCoordinates()
        elif x == 3:
            geneticAlgorithm()
        elif x == 4:
            ACO()
        elif x == 5:
            TSP()
        else:
            print("END")
            break
    else:
        print("END")
        break

