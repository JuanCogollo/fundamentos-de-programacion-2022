def is_british_flag(flag):
    for i in range(len(flag)):
        row = flag[i]

        if i == len(flag) // 2:
            if row[0][len(row[0]) // 2] != "#":
                return print('Ni idea')
        else:
            if row[0][len(row[0]) // 2] != "+":
                return print('Ni idea')

        if row[0][i] != "#" or row[0][-1 - i] != "#":
            return print('Ni idea')
        if i == len(flag) // 2:
            for k in range(len(row[0])):
                if k == len(row[0]) // 2:
                    if row[0][k] != "#":
                        return print('Ni idea')
                elif row[0][k] != "+":
                    return print('Ni idea')

    return print('Bandera britanica')


def main():
    flag = []

    c = int(input())

    for i in range(c):
        lines = int(input())
        for k in range(lines):
            row = input()
            row = row.split()
            flag.append(row)

        is_british_flag(flag)
        flag.clear()


main()
