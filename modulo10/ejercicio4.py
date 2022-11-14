def ewokes_translator(dictionary, word):
    try:
        print(dictionary[word])
    except:
        print('palabra no encontrada')


def main():
    ewokes_espanol = {}

    # numero de entradas
    n = int(input())

    for i in range(n):
        # entrada
        e = input()
        e = e.split(" ")
        ewokes_espanol[e[0]] = e[1]

    m = int(input())

    for i in range(m):
        word = input()
        ewokes_translator(ewokes_espanol, word)


main()
