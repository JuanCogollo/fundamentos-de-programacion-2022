import functools


def is_perfect(value):
    divisores = []
    for i in range(1, value):
        if value % i == 0 and i != value:
            divisores.append(i)
    total = functools.reduce(lambda a, b: a + b, divisores)
    if total == value:
        print(f'{value} es perfecto')
    else:
        print(f'{value} no es perfecto')


def main():
    values = int(input())

    for i in range(values):
        value = int(input())
        is_perfect(value)


if __name__ == '__main__':
    main()
