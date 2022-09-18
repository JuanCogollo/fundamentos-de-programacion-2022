def to_arr(int_):
    return [int(a) for a in str(int_)]


def hyperpar(value):
    arr = to_arr(value)
    arr_validations = []

    for num in arr:
        if num % 2 == 0:
            arr_validations.append(True)
    if len(arr_validations) == len(arr):
        print('Hyperpar')
    else:
        print('No es hyperpar')


def main():
    while True:
        value = input()
        if value == '-1':
            break
        else:
            hyperpar(value)


if __name__ == '__main__':
    main()
