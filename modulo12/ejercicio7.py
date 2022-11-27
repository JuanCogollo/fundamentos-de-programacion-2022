def mover_fila(cubo, fila, dir):
    fila -= 1

    if dir == "+":
        cubo[fila] = [cubo[fila][-1]] + cubo[fila][:-1]
    else:
        cubo[fila] = cubo[fila][1:] + [cubo[fila][0]]
    return cubo


def mover_columnas(cubo, col, dir):
    col -= 1
    size = len(cubo)
    new_col = []
    if dir == "+":
        new_col.append(cubo[-1][col])
        for fila in range(size - 1):
            new_col.append(cubo[fila][col])
    else:
        for fila in range(1, size):
            new_col.append(cubo[fila][col])
        new_col.append(cubo[0][col])

    for i in range(size):
        cubo[i][col] = new_col[i]

    return cubo


c = int(input())
for case in range(c):
    n = int(input())
    cubo = []
    for i in range(n):
        cubo.append(list(range(1, n + 1)))

    movs = input().split()
    for mov in movs:
        if mov[0] == "C":
            cubo = mover_columnas(cubo, int(mov[1]), mov[2])
        else:
            cubo = mover_fila(cubo, int(mov[1]), mov[2])

    for i in range(n):
        for j in range(n):
            print(cubo[i][j], end="")
        print()
    print()
