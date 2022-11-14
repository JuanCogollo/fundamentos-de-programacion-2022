def print_format(arr):
    for i in range(len(arr)):
        print(f'{i + 1} {arr[i][0]} {arr[i][1]}')


def get_insalubre(arr):
    insalubres = []
    for empleado in arr:
        IMC = round((float(empleado[1]) / float(empleado[2]) ** 2), 1)
        if (
                (IMC > 25) and
                float(empleado[3]) > 100 and
                float(empleado[4]) > 150
        ):
            empleado = [empleado[0], IMC]
            insalubres.append(empleado)

    insalubres.sort(key=lambda x: (x[1], x[0]), reverse=True)
    return insalubres


def main():
    data = []

    # numero de entradas
    n = int(input())

    for i in range(n):
        # entrada
        e = input()
        e = e.split(", ")
        data.append(e)

    print_format(get_insalubre(data))


main()
