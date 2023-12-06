#Initialise le tableau.
def newBoard(n):
    if n % 4 != 1:
        n = 9
    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                board[i][j] = 2
            else:
                board[i][j] = 1
    board[n // 2][n // 2] = 0
    return board

#Réalise l'affichage du plateau.
def displayBoard(board, n):
    print("    ", end='')
    for j in range(n):
        print(f"{j + 1:2} ", end='')
    print()
    for i in range(n):
        print(f"{i + 1:2} | ", end='')
        for j in range(n):
            if board[i][j] == 0:
                print(".  ", end='')
            elif board[i][j] == 1:
                print("o  ", end='')  # Les pions o pour le joueur 1
            elif board[i][j] == 2:
                print("x  ", end='')  # Les pions x pour le joueur 2
        print()
    print("\n")

#Verifie qu'un mouvement est possible.
def possiblePawn(board, n, player, i, j):
    if board[i][j] != player:
        return False
    if i > 0 and board[i - 1][j] == 0:
        return True
    if i < n - 1 and board[i + 1][j] == 0:
        return True
    if j > 0 and board[i][j - 1] == 0:
        return True
    if j < n - 1 and board[i][j + 1] == 0:
        return True
    return False

#Fait saisir au joueur les coordonnées d’un pion pouvant se déplacer.
def selectPawn(board, n, player):
    while True:
        print(f"Joueur {player}, sélectionnez un pion à déplacer :")
        try:
            i = int(input(f"Ligne (1-{n}): ")) - 1
            j = int(input(f"Colonne (1-{n}): ")) - 1
            if 0 <= i < n and 0 <= j < n and board[i][j] == player and possiblePawn(board, n, player, i, j):
                return i, j
            else:
                print("Les coordonnées sont invalides ou le mouvement est impossible, veuillez réessayer.")
        except (ValueError, IndexError):
            print("Les coordonnées sont invalides, veuillez réessayer.")

#Met un jour le tableau après un mouvement.
def updateBoard(board, n, i, j):
    if i > 0 and board[i - 1][j] == 0:
        board[i - 1][j] = board[i][j]
        board[i][j] = 0
    elif i < n - 1 and board[i + 1][j] == 0:
        board[i + 1][j] = board[i][j]
        board[i][j] = 0
    elif j > 0 and board[i][j - 1] == 0:
        board[i][j - 1] = board[i][j]
        board[i][j] = 0
    elif j < n - 1 and board[i][j + 1] == 0:
        board[i][j + 1] = board[i][j]
        board[i][j] = 0

#Verifie que le joueur peut encore se déplacer.
def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if board[i][j] == player and possiblePawn(board, n, player, i, j):
                return True
    return False

#Demande à l'utilisateur la taille du tableau.
def getBoardSize():
    while True:
        try:
            n = int(input("Entrez la taille du tableau (5, 9, 13 ou 17) : "))
            if n in [5, 9, 13, 17]:
                return n
            else:
                print("Vous devez entrer une taille de tableau valide (5, 9, 13 ou 17).")
        except ValueError:
            print("Vous devez entrer un nombre entier valide.")

#Execute le jeu.
def lewthwaite():
    n = getBoardSize()

    board = newBoard(n)
    player = 1
    first_turn = True

    while first_turn or again(board, n, player):
        first_turn = False
        displayBoard(board, n)
        i, j = selectPawn(board, n, player)
        updateBoard(board, n, i, j)
        player = 3 - player

    displayBoard(board, n)
    if not again(board, n, player):
        print(f"Le joueur {player} a perdu, il ne peut plus se déplacer. Le joueur {3 - player} a gagné!")

lewthwaite()