month_to_num = {
    "enero": 13,
    "febrero": 14,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

num_to_date = {
    0: "sabado",
    1: "domingo",
    2: "lunes",
    3: "martes",
    4: "miercoles",
    5: "jueves",
    6: "viernes"
}


def y(year, month):
    if month == month_to_num["enero"] \
            or month == month_to_num["febrero"]:
        return year - 1
    return year


def zeller(arr):
    d = arr[0]
    m = arr[1]
    year = y(arr[2], m)
    day = int((
                      d
                      + ((13 * (m + 1)) // 5)
                      + year
                      + (year // 4)
                      - (year // 100)
                      + (year // 400)
              ) % 7)

    return num_to_date[day]


def main():
    c = int(input())

    for i in range(c):
        date = input()
        date = date.split("-")
        date[0], date[1], date[2] = \
            int(date[0]), month_to_num[date[1]], int(date[2])

        print(zeller(date))


main()

