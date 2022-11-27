def verificarFilas(sudoku):
    test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for fila in sudoku:
        if test != sorted(fila):
            return False
    return True


def verificarColumas(sudoku):
    test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for col in range(9):
        columna = []
        for fila in sudoku:
            columna.append(fila[col])
        if test != sorted(columna):
            return False
    return True


def verificarSub(sudoku):
    test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(3):
        for j in range(3):
            sub = []
            for fila in range(3 * i, 3 * i + 3):
                for col in range(3 * j, 3 * j + 3):
                    sub.append(sudoku[fila][col])
            if test != sorted(sub):
                return False
    return True


c = int(input())
for case in range(c):
    caso = input()

    sudoku = []
    for i in range(9):
        fila = input().split()
        sudoku.append(fila)

    if verificarFilas(sudoku) and verificarColumas(sudoku) and verificarSub(sudoku):
        print("Resuelto")
    else:
        print("No resuelto")
