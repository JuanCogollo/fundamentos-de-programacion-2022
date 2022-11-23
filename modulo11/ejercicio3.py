from random import randint


def winner(pc):
    lanzamiento = randint(1, 6) + randint(1, 6)
    if lanzamiento > pc:
        print("Gana el humano")
    elif pc > lanzamiento:
        print("Gana la plataforma")
    else:
        print("Empate")


def main():
    c = int(input())

    for i in range(c):
        entry = input()
        num = int(entry.split(" ")[1])
        winner(num)


main()
