def main():
    partidos_jugados = int(input())

    goles_ballenota = []
    goles_mandril = []

    ballenota_fc = 0
    real_mandril_fc = 0

    for i in range(partidos_jugados):
        goles_ballenota += [int(input())]
    for j in range(partidos_jugados):
        goles_mandril += [int(input())]

    for k in range(partidos_jugados):
        if goles_ballenota[k] == goles_mandril[k]:
            ballenota_fc += 1
            real_mandril_fc += 1
        if goles_ballenota[k] > goles_mandril[k]:
            ballenota_fc += 2
        if goles_mandril[k] > goles_ballenota[k]:
            real_mandril_fc += 2

    print(f'Ballenota Futbol Club: {ballenota_fc}')
    print(f'Real Mandril: {real_mandril_fc}')


if __name__ == '__main__':
    main()
