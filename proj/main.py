from proj.aco import ACO
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
    print("3 - algortym genetyczny")
    print("4 - ant colony optimization")
    print("_ - koniec")

    x = input("Wybierz wariant: ")
    if x.isnumeric():
        x = int(x)
        if x == 1:
            n = int(input("Podaj ilość punktów: "))
            generateCoordinates(n)
        elif x == 2:
            printCoordinates()
        elif x == 3:
            geneticAlgorithm()
        elif x == 4:
            ACO()
        else:
            print("KONIEC")
            break
    else:
        print("KONIEC")
        break