def panvocalica(str):
    if (
            'a' in str
            and 'e' in str
            and 'i' in str
            and 'o' in str
            and 'u' in str
    ):
        print('Panvocalica')
    else:
        print('No es panvocalica')


def main():
    n = int(input())
    for i in range(n):
        palabra = input()
        panvocalica(palabra)


main()
