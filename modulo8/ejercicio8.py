
def carta(v, p):
    new_carta = [v, p]
    return new_carta


def main():

    cartas = []

    M = int(input())

    for k in range(M):
        counter = 0
        while counter < 5:
            v = int(input())
            p = input()
            cartas.append(carta(v, p))
            # print('Carta:', cartas[-1])
            # print('Cartas', cartas)
            counter += 1

        print('Evaluation unimplemented.')


if __name__ == '__main__':
    main()

# ej

# 2

# mano 1
# 7
# D
# 6
# C
# 9
# T
# 8
# P
# 5
# T
# escalera normal

# mano 2
# 11
# C
# 10
# C
# 13
# C
# 14
# C
# 12
# C
# escalera real
