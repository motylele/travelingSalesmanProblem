from proj.aco import aco
from proj.geneticAlgorithm import geneticAlgorithm
from utils.coordinatesFun import generateCoordinates, printCoordinates

while 1:
    print("Mateusz Motyl")
    print("Inf. Dz. II st.")
    print("ind: 269381\n\n")

    print("Rozwiązywanie problemu komiwojażera")
    print("Wybór wariantów:")
    print("1 - wygeneruj nowe punkty")
    print("2 - pokaż wygenerowane punkty")
    print("3 - alg. gen.")
    print("4 - ACO")
    print("5 - koniec")

    x = int(input("Wybierz wariant: "))
    if x == 1:
        n = int(input("Podaj ilość punktów: "))
        generateCoordinates(n)
    elif x == 2:
        printCoordinates()
    elif x == 3:
        geneticAlgorithm()
    elif x == 4:
        aco()
    else:
        print("KONIEC")
        break