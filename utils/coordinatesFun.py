from os import system
import numpy as np

def generateCoordinates(n): #len of Pl borders = 3573
    coordinates = [[x, y] for x, y in zip(np.random.uniform(49.3, 54.8, n), #latitude of Pl
                                        np.random.uniform(14.2, 23.9, n))] #longitude of Pl
    with open("\INF-D-2023-Mateusz-Motyl-269381\\utils\cords.txt", "w") as f:
        for item in coordinates:
            f.write(str(item) + "\n")
    f.close()
    print("Wygenerowano nowe współrzędne")
    n = input("Naciśnij klawisz, żeby powrócić ")
    system("cls")

def printCoordinates():
    with open("\INF-D-2023-Mateusz-Motyl-269381\\utils\cords.txt", "r") as f:
        for count, line in enumerate(f):
            print(line, end="")
        print("Liczba punktów: " + str(count + 1))
    f.close()

    n = input("Naciśnij klawisz, żeby powrócić ")
    system("cls")

