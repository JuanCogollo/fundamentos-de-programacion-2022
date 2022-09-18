def P(x):
    return 2 * x + 1


def A(x):
    return 3 ** x


def N(x):
    import math
    return math.sqrt(5 * x + 4)


def main():
    values = int(input())

    for i in range(values):
        value = float(input())
        print(P(A(N(value))))


if __name__ == '__main__':
    main()
