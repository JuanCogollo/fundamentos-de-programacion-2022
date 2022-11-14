import functools


def print_format(arr):
    for i in arr:
        print(f'{i[0]} {i[1]}')


def calificacion(arr):
    for notes in arr:
        cantidad_ejercicios = [9, 11, 12, 8, 12, 9, 11, 8, 11, 10, 9, 10]
        for i in range(len(notes)):
            notes[i] = round(((int(notes[i]) / cantidad_ejercicios[i]) * 5), 1)

    return arr


def promedio(arr):
    data = []
    for i in range(len(arr)):
        data.append([arr[i][0]])
        arr[i].pop(0)

    calificaciones_arr = calificacion(arr)

    for i in range(len(data)):
        data[i] \
            .append(
            functools
            .reduce(lambda a, b: a + b, (calificaciones_arr[i])) / 12
        )

    for d in data:
        d[1] = round(d[1], 1)

    data.sort(key=lambda x: x[0])
    return data


def main():
    data = []

    # numero de entradas
    n = int(input())

    for i in range(n):
        # entrada
        e = input()
        e = e.split(", ")
        data.append(e)

    print_format(promedio(data))


main()
