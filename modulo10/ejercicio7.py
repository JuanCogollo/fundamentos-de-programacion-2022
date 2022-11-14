def winner(data_):
    data = data_

    winner_employee = list(data)[0]
    for employee in data:
        if data[winner_employee] < data[employee]:
            winner_employee = employee

    return winner_employee


def main():
    employees = {}
    c = int(input())

    for i in range(c):
        entry = input()
        data = entry.split(": ")
        try:
            employees[data[0]] += int(data[1])
        except:
            employees[data[0]] = int(data[1])

    result = winner(employees)
    print(f'El vendedor del mes es {result}')


main()
