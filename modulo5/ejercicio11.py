def main():
    a = int(input())  # polifactor?
    p = int(input())  # primer número
    q = int(input())  # segundo número

    polifactor = True

    _a = a

    for i in range(p, q + 1):
        quotient, modulo_a = divmod(_a, i)
        _a = quotient
        if modulo_a != 0:
            polifactor = False
            print(f'{a} no es polifactor entre {p} y {q}')
            break

    if polifactor:
        print(f'{a} es polifactor entre {p} y {q}')


if __name__ == '__main__':
    main()
