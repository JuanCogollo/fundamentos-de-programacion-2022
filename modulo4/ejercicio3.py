def main():
    x = float(input())
    y = float(input())
    z = float(input())

    numsArr = [x, y, z]
    orderedArr = sorted(numsArr)

    print(f'{orderedArr[1]} es la mediana')


if (__name__ == '__main__'):
    main()
