
def flag_printer(value):
    flag = ''

    for k in range(value):
        for i in range(value):
            if k == i or i + k == value - 1:
                flag += '#'
            else:
                flag += '0'

        flag += '\n'

    print(flag)


def main():
    while True:
        ld = int(input())
        if ld != 0:
            flag_printer(ld)
        else:
            break


if __name__ == '__main__':
    main()
