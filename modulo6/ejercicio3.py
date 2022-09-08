def main():
    cromos = []

    cromo_id = 1

    while cromo_id != 0:
        cromo_id = int(input())
        cromos.append(cromo_id)

    cromos.pop()
    print(len(set(cromos)))


if __name__ == '__main__':
    main()
