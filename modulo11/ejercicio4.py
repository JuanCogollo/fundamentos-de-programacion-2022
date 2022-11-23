def time_parser(time):
    time_, tz = time.split(" ")
    h, m, s = time_.split(":")
    h, m, s = int(h), int(m), int(s)

    if h == 12 and tz == "AM":
        h -= 12

    if tz == "PM" and h != 12:
        h = int(h) + 12

    return (h * 60 * 60) + (m * 60) + s


def left(time):
    DAY = 86400
    time_parsed = time_parser(time)
    return round((time_parsed * 100) / DAY, 3)


def main():
    c = int(input())

    for i in range(c):
        entry = input()
        result = left(entry)

        print(f"Loading day ... {result}%")


main()
