def str_to_arr(str):
    arr = []
    for i in range(len(str)):
        arr.append(str[i])
    return arr


def is_armstrong(value):
    nums = str_to_arr(value)
    value_int = int(value)
    sum = 0

    for i in range(len(nums)):
        index_int = int(nums[i])
        sum += index_int**len(nums)

    if value_int == sum:
        print(f'{value_int} es Armstrong')
    else:
        print(f'{value_int} no es Armstrong')


def main():

    vals = int(input())

    for i in range(vals):
        value = input()
        is_armstrong(value)


if __name__ == '__main__':
    main()
