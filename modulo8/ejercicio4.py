

def sum_lst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


def espejos(arr):
    espejos = 0
    for i in range(1, len(arr)):
        lst_1 = arr[:i]
        lst_2 = arr[i:]
        sum_lst_1 = sum_lst(lst_1)
        sum_lst_2 = sum_lst(lst_2)
        if sum_lst_1 == sum_lst_2:
            espejos += 1

    return espejos


def main():

    vals = int(input())
    lst = []

    for i in range(vals):
        val = float(input())
        lst.append(val)

    print(espejos(lst))


if __name__ == '__main__':
    main()
