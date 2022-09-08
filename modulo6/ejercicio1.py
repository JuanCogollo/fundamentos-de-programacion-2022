def main():

    num_seen = int(input())
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0

    for i in range(num_seen):
        num = int(input())
        if num == 1:
            n1 += 1
        elif num == 2:
            n2 += 1
        elif num == 3:
            n3 += 1
        elif num == 4:
            n4 += 1
        elif num == 5:
            n5 += 1

    print(f'1: {n1}')
    print(f'2: {n2}')
    print(f'3: {n3}')
    print(f'4: {n4}')
    print(f'5: {n5}')


if __name__ == '__main__':
    main()
