def str_to_num(arr, idx):
    new_arr = []
    for i in range(len(arr)):
        arr[i][idx] = int(arr[i][idx])
        new_arr.append(arr[i])

    return new_arr


def print_format(arr):
    for i in arr:
        print(f'{i[0]} {i[1].upper()} {i[2]}')


def ordering(arr):
    arr_cleaned = []
    arr = str_to_num(arr, 3)
    arr = str_to_num(arr, 1)
    for i in range(len(arr)):
        if arr[i][2] == 'positiva':
            arr_cleaned.append(arr[i])
        else:
            continue

    arr_cleaned.sort(key=lambda x: (x[3], x[1]), reverse=True)

    for i in range(len(arr_cleaned)):
        arr_cleaned[i].pop(0)

    return arr_cleaned


def main():
    data = []

    ciudadanos = int(input())

    for i in range(ciudadanos):
        ciudadano = input()
        data.append(ciudadano.split(" "))

    print_format(ordering(data))


main()
