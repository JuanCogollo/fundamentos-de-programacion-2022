def main():
    salarios_input = 1
    salarios_arr = []

    while salarios_input != 0:
        salarios_input = int(input())
        salarios_arr.append(salarios_input)

    salarios_arr.pop()
    salarios_arr.sort()
    indice_de_desigualdad = (salarios_arr[-3] - salarios_arr[2]) / len(salarios_arr)**2
    print(round(indice_de_desigualdad, 2))


if __name__ == '__main__':
    main()
