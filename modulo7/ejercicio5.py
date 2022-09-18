import math


def f(x):
    return math.sqrt(2 + (5 * x))


def g(x):
    return (4 + x) ** 3


def main():

    while True:
        value = float(input())
        if value == 0:
            break
        elif value % 2 == 0:
            print(f(g(value)))
        else:
            print(g(f(value)))


if __name__ == '__main__':
    main()
