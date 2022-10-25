def arr_from(str_):
    return str_.split(' ')


def circle(arr):
    F = 0
    M = 0
    for par in arr:
        for letra in par:
            if letra == 'F':
                F += 1
            elif letra == 'M':
                M += 1

    if F == M:
        print('Es posible hacer un unico circulo')
    else:
        print('No es posible')


def main():
    n = int(input())
    for i in range(n):
        cables = input()
        circle(arr_from(cables))


main()
