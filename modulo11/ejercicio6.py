from datetime import datetime, timedelta


def how_many_days(arr, day):
    for range_c in arr:
        count = 0
        birth, age = range_c[0], range_c[1]
        for i in range(age):
            if birth.strftime("%A") == day:
                count += 1
            birth += timedelta(days=365)

        print(count)


def main():
    c = int(input())
    date_ranges = []

    for i in range(c):
        d = input()
        birth_date, age = d.split(" ")
        date_ranges.append([datetime.strptime(birth_date, "%Y/%m/%d"), int(age)])

    how_many_days(date_ranges, "Monday")


main()
