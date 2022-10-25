def escalera_normal(cartas):
    for i in range(1, 5):
        if cartas[i][0] != cartas[i - 1][0] + 1:
            return False
    return True


def color(cartas):
    for i in range(len(cartas)):
        if cartas[i][1] != cartas[i - 1][1]:
            return False
    return True


def escalera_color(cartas):
    if escalera_normal(cartas) and color(cartas):
        return True
    return False


def escalera_real(cartas):
    val = 10
    for i in range(len(cartas)):
        if (
                cartas[i][0] != val
                or
                cartas[i][1] != cartas[i - 1][1]
        ):
            return False
        val += 1
    return True


def carta(v, p):
    return [v, p]


def what_it_is(cartas):
    cartas_sorted = sorted(cartas)
    if escalera_real(cartas_sorted):  # consecutivas 10..14 | mismo palo
        return print('Escalera real')
    elif escalera_color(cartas_sorted):  # consecutivas
        return print('Escalera de color')
    elif escalera_normal(cartas_sorted):  # consecutivas
        return print('Escalera normal')
    elif color(cartas_sorted):  # mismo palo
        return print('Color')
    else:
        return print('Otra mano')


def main():
    cartas = []

    M = int(input())

    for k in range(M):
        counter = 0
        while counter < 5:
            v = int(input())
            p = input()
            cartas.append(carta(v, p))
            # print('Carta:', cartas[-1])
            # print('Cartas', cartas)
            counter += 1

        what_it_is(cartas)
        cartas.clear()


if __name__ == '__main__':
    main()
