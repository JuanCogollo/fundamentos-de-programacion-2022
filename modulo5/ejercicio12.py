def main():

    days = int(input())
    total_born = 0

    for i in range(1, days + 1):
        prom = float(input())
        born = (prom * i) - total_born
        total_born += born
        print(int(born))


if __name__ == '__main__':
    main()
