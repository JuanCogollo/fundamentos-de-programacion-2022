def main():
    x = float(input())
    how_many = 0

    while x >= 10:
        x /= 2
        how_many += 1

    print(how_many)


if __name__ == '__main__':
    main()
