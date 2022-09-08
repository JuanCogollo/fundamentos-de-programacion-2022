def main():
    tarifa = int(input())
    horas = int(input())

    if horas > 45:
        pago = int((tarifa * 45) + ((horas - 45) * (tarifa * 1.5)))
        print(f'$ {pago}')
    else:
        pago = int(tarifa * horas)
        print(f'$ {pago}')


if __name__ == '__main__':
    main()
