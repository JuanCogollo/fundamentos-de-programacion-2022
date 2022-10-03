def main():

    days = int(input())
    total_born = 0

    for i in range(1, days + 1): # 1 => 6 + 1
        prom = float(input())
        # promedio * numero_de_dia - total_de_nacidos
        nacidos_ese_dia = (prom * i) - total_born
        total_born += nacidos_ese_dia
        print(int(nacidos_ese_dia))


if __name__ == '__main__':
    main()
