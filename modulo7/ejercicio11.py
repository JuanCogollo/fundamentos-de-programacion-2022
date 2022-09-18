import functools
from math import factorial


def to_arr(int_):
    return [int(a) for a in str(int_)]


def is_fuerte(value):
    num_arr = to_arr(value)
    factorial_arr = []
    for num in num_arr:
        factorial_arr.append(factorial(num))

    total = functools.reduce(lambda a, b: a + b, factorial_arr)

    if total == value:
        print(f'{value} es fuerte')
    else:
        print(f'{value} no es fuerte')


def main():
    values = int(input())

    for i in range(values):
        value = int(input())
        is_fuerte(value)


if __name__ == '__main__':
    main()
