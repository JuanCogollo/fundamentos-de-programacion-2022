
def mul_matriz(m1, m2):
    matriz = []
    for i in range(len(m1)):
        matriz.append([0] * len(m2[0]))

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matriz[i][j] += m1[i][k] * m2[k][j]

    for l in matriz:
        print(" ".join([str(elem) for elem in l]))


def main():
    #
    m1 = input()
    m1_row, m1_col = m1.split("x")
    m1_row, m1_col = int(m1_row), int(m1_col)
    #
    m2 = input()
    m2_row, m2_col = m2.split("x")
    m2_row, m2_col = int(m2_row), int(m2_col)

    if m1_col != m2_row:
        return print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")

    matriz_1 = []
    matriz_2 = []
    for i in range(m1_row):
        aux = []
        for k in range(m1_col):
            n = int(input())
            aux.append(n)

        matriz_1.append(aux)

    for i in range(m2_row):
        aux = []
        for k in range(m2_col):
            n = int(input())
            aux.append(n)

        matriz_2.append(aux)

    mul_matriz(matriz_1, matriz_2)


main()
