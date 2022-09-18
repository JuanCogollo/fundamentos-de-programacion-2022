def main():
    numero_de_fichas = int(input())

    fichas = []

    for i in range(numero_de_fichas - 1):
        ficha = int(input())
        fichas.append(ficha)

    fichas.sort()

    for i in range(numero_de_fichas):
        try:
            if fichas[i] != i + 1:
                print(f'La ficha faltante es la {i + 1}')
                break
        # The line above is not a recomended implementation, but works
        except:
            print(f'La ficha faltante es la {i + 1}')
            break


if __name__ == "__main__":
    main()
