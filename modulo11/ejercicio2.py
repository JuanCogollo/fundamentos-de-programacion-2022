from datetime import datetime


def printer(result):
    print(f'true vampires {result["true vampires"]}')
    print(f'early birds {result["early birds"]}')
    print(f'sunny warmers {result["sunny warmers"]}')
    print(f'lunch workers {result["lunch workers"]}')
    print(f'sunset lovers {result["sunset lovers"]}')
    print(f'prime timers {result["prime timers"]}')


def programmers_schedule(times_arr):
    qualy = {
        "true vampires": 0,
        "early birds": 0,
        "sunny warmers": 0,
        "lunch workers": 0,
        "sunset lovers": 0,
        "prime timers": 0
    }

    for time in times_arr:
        time_parsed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        date = time.split(" ")[0]
        if (datetime.strptime(f"{date} 00:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 03:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["true vampires"] += 1
        elif (datetime.strptime(f"{date} 04:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 07:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["early birds"] += 1
        elif (datetime.strptime(f"{date} 08:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 11:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["sunny warmers"] += 1
        elif (datetime.strptime(f"{date} 12:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 15:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["lunch workers"] += 1
        elif (datetime.strptime(f"{date} 16:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 19:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["sunset lovers"] += 1
        elif (datetime.strptime(f"{date} 20:00:00", '%Y-%m-%d %H:%M:%S') <= time_parsed <= datetime.strptime(
                f"{date} 23:59:59", '%Y-%m-%d %H:%M:%S')):
            qualy["prime timers"] += 1

    return qualy


def main():
    c = int(input())

    commiting_times = []

    for i in range(c):
        entry = input()
        commiting_times.append(entry)

    result = programmers_schedule(commiting_times)
    printer(result)


main()

