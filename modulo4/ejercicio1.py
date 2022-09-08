def main():
    tarifa = int(input())
    horasTrab = int(input())

    horasExt = horasTrab - 45

    if horasExt <= 0:
        print(f'$ {horasTrab * tarifa}')

    else:
        pagoExt = (tarifa * 1.5) * horasExt
        pagoTotal = (45 * tarifa) + pagoExt
        print(f'$ {int(pagoTotal)}')


if __name__ == '__main__':
    main()
