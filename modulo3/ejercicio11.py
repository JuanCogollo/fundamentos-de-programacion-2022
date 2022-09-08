def main():
    n = int(input())

    if n == 3:
        print('El numero 3 es el mejor')
    elif n % 3 == 0:
        print(f'El numero {n} es multiplo de 3. Y el numero 3 es el mejor')
    elif (n + 1) % 3 == 0:
        print(f'El numero {n} no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor')
    elif (n - 1) % 3 == 0:
        print(
            f'El numero {n} no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')


if __name__ == '__main__':
    main()
