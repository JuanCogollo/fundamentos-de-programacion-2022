def main():
    suma = 35
    cont = 0
    for i in range(2, 12, 2):
        for j in range(i // 2, i + 1):
            suma += j
            cont += 1
    resultado = suma - 5 * cont
    print(resultado)


if __name__ == '__main__':
    main()
