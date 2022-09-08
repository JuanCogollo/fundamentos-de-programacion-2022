def main():
    c = int(input())
    k = int(input())
    renta = k - c

    if renta == 0:
        print('No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero')

    retorno = (((k - c) / c) * 100)

    if renta > 0:
        print(f'Hubo una ganancia de $ {renta} correspondiente al {retorno} % del capital invertido')

    if renta < 0:
        print(f'Hubo una perdida de $ {renta * -1} correspondiente al {retorno * -1} % del capital invertido')


if __name__ == '__main__':
    main()
