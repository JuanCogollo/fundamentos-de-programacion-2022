def main():
    total_sq = int(input())
    side = float(input())
    increment = float(input())
    area = 0

    for i in range(total_sq):
        area += side ** 2
        side += increment

    print(f'El area total es de {area} metros cuadrados')


if __name__ == '__main__':
    main()
