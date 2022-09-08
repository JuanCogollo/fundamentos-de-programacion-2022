def main():
    C = int(input())
    N = int(input())

    if (
            (C % 13 == 0 or C % 23 == 0)
            or
            (N % 13 == 0 or N % 23 == 0)
    ):
        print(f'La direccion calle {C} # {N} esta prohibida')
    else:
        print(f'La direccion calle {C} # {N} no esta prohibida')


if __name__ == '__main__':
    main()
