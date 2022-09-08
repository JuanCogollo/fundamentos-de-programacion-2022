def main():
    max_capability = float(input())
    elephants_amount = int(input())

    how_many_elephants = 0
    max_weight = 0

    for i in range(elephants_amount):
        max_weight += float(input())
        if max_weight <= max_capability:
            how_many_elephants += 1
        else:
            continue

    print(how_many_elephants)


if __name__ == '__main__':
    main()
