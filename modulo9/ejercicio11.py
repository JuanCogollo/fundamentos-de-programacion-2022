def to_arr(string):
    return [str(a) for a in str(string)]


def flatten(list_):
    return [item for sublist in list_ for item in sublist]


def is_trifelio(file):
    for line in file:
        words = line.split('-')
        words[1] = words[1].replace('\n', '')

        first_word = words[1]

        if (
                (first_word ==
                 (words[0][(int(len(words[0]) / 2)):]
                  + words[0][:(int(len(words[0]) / 2))])) or
                (first_word ==
                 (words[0][(int(len(words[0]) / 2)) + 1:])
                 + (words[0][:(int(len(words[0]) / 2) + 1)])) or
                (first_word ==
                 (words[0][(int(len(words[0]) / 2)) - 1:]
                  + words[0][:(int(len(words[0]) / 2)) - 1]))
        ):
            print('Es trifelio')

        else:
            print('No es trifelio')


def main():
    # file = open("files/trifelios.txt", "r")
    file = open("trifelios.txt", "r")  # todo: ticademia version
    is_trifelio(file)

    file.close()


main()



