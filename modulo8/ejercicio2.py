def lucas_serie(max):
    lucas_list = [2, 1]
    while lucas_list[-1] <= max:
        lucas_list.append(lucas_list[-1] + lucas_list[-2])
    return lucas_list


def main():

    val_1 = int(input())
    val_2 = int(input())

    lucas = lucas_serie(val_2)

    matches = 0
    for i in range(val_1, val_2 + 1):
        if i in lucas:
            matches += 1

    print(matches)


if __name__ == '__main__':
    main()
