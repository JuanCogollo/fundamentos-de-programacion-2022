def main():
    v = int(input())
    e = int(input())
    cambio = e - v

    if ((cambio % 10 == 0 or cambio % 15 == 0)
            and
            (cambio % 4 == 0)):

        print(cambio)

    elif ((cambio % 10 == 0 or cambio % 15 == 0)
          and
          not (cambio % 4 == 0)):

        print(cambio)
        print('y te lo puedes quedar')


if __name__ == '__main__':
    main()
