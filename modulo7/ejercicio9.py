def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))


def main():
    values = int(input())

    for i in range(values):
        m = int(input())
        n = int(input())
        print(A(m, n))


if __name__ == '__main__':
    main()
