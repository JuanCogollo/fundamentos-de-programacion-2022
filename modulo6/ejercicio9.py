def main():
    id_personas = []
    suman_1995 = 0

    stopper = 1
    while stopper != 0:
        stopper = int(input())
        id_personas.append(stopper)

    id_personas.pop()

    for i in id_personas:
        if 1995 - i in id_personas:
            suman_1995 += 1

    print(suman_1995 / 2)


if __name__ == "__main__":
    main()
