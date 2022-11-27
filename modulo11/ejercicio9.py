from calendar import Calendar
from datetime import datetime


def print_calendar(date):
    days = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
    month = date.month
    year = date.year
    c = Calendar(firstweekday=0)
    cal_arr = c.monthdayscalendar(year=year, month=month)
    cal_arr = list(map(lambda x: list(map(lambda y: y if y != 0 else "", x)), cal_arr))
    cal_arr.insert(0, days)
    print("\n".join(map(lambda x: "\t".join(map(str, x)), cal_arr)))


def main():
    c = int(input())
    for i in range(c):
        d = input()
        date = datetime.strptime(d, "%d/%m/%Y")
        print_calendar(date)


main()
