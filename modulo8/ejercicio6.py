
def finding_multidigit(int):
    str_from_int = str(int)

    if (str_from_int.__contains__('1') and
        str_from_int.__contains__('2') and
        str_from_int.__contains__('3') and
        str_from_int.__contains__('4') and
            str_from_int.__contains__('5')):

        print("Multidigito")
    else:
        print("No es multidigito")


def main():

    while True:
        num = int(input())
        if num != 0:
            finding_multidigit(num)
        else:
            break


if __name__ == '__main__':
    main()
