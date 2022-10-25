def arr_from(str_):
    return str_.split(' ')


def mas_viejo(arr):
    placa_julian = arr[0]
    arr_sorted = sorted(arr)
    if arr_sorted[0] == placa_julian:
        print('Mi cacharrito es el mas viejo de todos los autos ;D')
    else:
        print('Al menos otro auto es mas viejo que mi cacharrito :(')


def main():
    n = int(input())
    for i in range(n):
        placas = input()
        mas_viejo(arr_from(placas))


main()
