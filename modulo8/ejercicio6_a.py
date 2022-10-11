
def finding_multidigit_of_5(int):
    str_from_int = str(int)

    match = 0
    for i in range(1, 6):
        if str_from_int.__contains__(str(i)):
            match += 1

    if (match >= 5):
        print("Multidigito")
    else:
        print("No es multidigito")


def main():

    while True:
        num = int(input())
        if num != 0:
            finding_multidigit_of_5(num)
        else:
            break


if __name__ == '__main__':
    main()
