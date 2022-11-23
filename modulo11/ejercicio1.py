from datetime import datetime


def duration(initial, end):
    initial = datetime.strptime(initial, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')

    dif = end - initial

    days = dif.days
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return (
        days,
        hours,
        minutes,
        seconds
    )


def main():
    c = int(input())

    results = []

    for i in range(c):
        entry = input()
        entry = entry.split(" ")
        initial_date, end_date = entry[1], entry[2]

        results.append(duration(initial_date, end_date))

    for r in results:
        days, hours, minutes, seconds = r
        print(f'{days} dias = {hours} horas = {minutes} minutos = {seconds} segundos')


main()

