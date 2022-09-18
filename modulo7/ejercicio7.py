def daniel_func(value):
    if value % 123 == 0:
        return 0
    else:
        return 1 + daniel_func(value + 23)


def main():
    values = int(input())

    for i in range(values):
        value = int(input())
        print(daniel_func(value))


if __name__ == '__main__':
    main()
