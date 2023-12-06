import random

#Initialise le tableau.
def newBoard(n, p):
    return [random.randint(0, p) for _ in range(n)]

#Réalise l’affichage du plateau.
def display(board, n):
    print()
    for i in range(n):
        print(f"{board[i]} |", end=" ")
    print("\n" + "-" * (n * 4))

    for i in range(n):
        print(f"{i + 1} |", end=" ")
    print("\n")

#Verifie si le numéro d’une case contient un pion déplaçable.
def possibleSquare(board, n, i):
    return 0 < i < n and board[i] > 0

#Fait saisir le numéro d’une case contenant un pion déplaçable.
def selectSquare(board, n):
    while True:
        try:
            i = int(input("Saisissez le numéro de la case contenant un pion déplaçable : ")) - 1
            if possibleSquare(board, n, i):
                return i
            else:
                print("Case invalide. Réessayez.")
        except ValueError:
            print("Il faut entrer un entier valide.")

#Vérifie si le déplacement est possible.
def possibleDestination(board, n, i, j):
    return 0 <= j < n and j < i and board[i] > 0

#Fait saisir le numéro d’une case vers laquelle se déplacer.
def selectDestination(board, n, i):
    while True:
        try:
            j = int(input(f"Saisissez le numéro de la case de destination pour le pion de la case {i + 1} : ")) - 1
            if possibleDestination(board, n, i, j):
                return j
            else:
                print("Destination invalide. Réessayez.")
        except ValueError:
            print("Il faut rentrer un entier valide.")

#Réalise le déplacement du pion.
def move(board, i, j):
    board[j] += 1
    board[i] -= 1

#Verifie si il y encore un déplacement possible.
def lose(board, n):
    return all(board[i] == 0 for i in range(1, n))

#Exécute le jeu.
def nimble():
    n = 0
    while n <= 0:
        try:
            n = int(input("Entrez la taille du plateau : "))
            if n <= 0:
                print("Entrez un entier strictement positif.")
        except ValueError:
            print("Il faut entrer un entier valide.")

    p = 0
    while p <= 0:
        try:
            p = int(input("Entrez le nombre maximal de pions par case : "))
            if p <= 0:
                print("Entrez un entier strictement positif.")
        except ValueError:
            print("Il faut entrer un entier valide.")

    board = newBoard(n, p)
    player = 1

    while not lose(board, n):
        display(board, n)
        print(f"Joueur {player}, c'est à vous de jouer .")

        i = selectSquare(board, n)
        j = selectDestination(board, n, i)
        move(board, i, j)

        player = 3 - player

    print()
    print(f"Le joueur {player} a perdu, il ne peut plus bouger de pions. Le joueur {3 - player} a gagné!")

nimble()