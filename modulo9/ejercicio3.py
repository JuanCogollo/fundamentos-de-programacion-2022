def procedence(str):
    if str[-2:] == 'ix':
        print('Galo')
    elif str[-2:] == 'us':
        print('Romano')
    elif str[-2:] == 'ic':
        print('Godo')
    elif str[-2:] == 'as':
        print('Griego')
    elif str[-2:] == 'af':
        print('Normando')
    elif str[-2:] == 'is' or str[-2:] == 'ax':
        print('Breton')
    elif str[-2:] == 'ez':
        print('Hispano')
    elif str[-1] == 'a':
        print('Indio')
    else:
        print('Desconocido')


def main():
    n = int(input())

    for i in range(n):
        name = input()
        procedence(name)


main()
