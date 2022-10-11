def julianachi(num):
    serie = [1]
    # for i in range(num):
    while serie[-1] <= num:
        div = 0
        for k in range(1, serie[-1] + 1):
            if serie[-1] % k == 0:
                div += 1
        serie.append(serie[-1] + div)

    return serie


def main():

    serie = julianachi(5000)

    while True:
        num = int(input())
        if num != 0:
            if num in serie:
                print('Pertenece a la serie de Julianachi')
            else:
                print('No pertenece a la serie de Julianachi')
        else:
            break


if __name__ == '__main__':
    main()
