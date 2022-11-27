from datetime import datetime


def time_elapsed_to_shipwrecked_time(days_elapsed):
    five, one = divmod(days_elapsed, 5)
    to_print = []
    for i in range(five):
        to_print.append("5")
    for i in range(one):
        to_print.append("1")

    print(" ".join(to_print))


def main():
    c = int(input())
    for i in range(c):
        d = input()
        start, end = d.split(" ")
        start, end = \
            datetime.strptime(start, "%d-%m-%Y"), \
            datetime.strptime(end, "%d-%m-%Y")
        days_elapsed = (end - start).days
        time_elapsed_to_shipwrecked_time(days_elapsed)


main()
