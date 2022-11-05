import re


def flatten(list_):
    return [item for sublist in list_ for item in sublist]


def causativos(line_):
    palabras_causativas = ['por tanto', 'dado que',
                           'por consiguiente', 'asi pues', 'por ende']
    matches = []
    for i in range(len(palabras_causativas)):
        matches.append(re.findall(palabras_causativas[i], line_))

    return len(flatten(matches))


def opositivos(line_):
    palabras_opositivas = ['sin embargo',
                           'no obstante', 'ahora bien', 'aun asi']
    matches = []
    for i in range(len(palabras_opositivas)):
        matches.append(re.findall(palabras_opositivas[i], line_))

    return len(flatten(matches))


def opositivos_causativos(file):
    for line in file:
        line = line.lower()
        print(f'Opositivos {opositivos(line)} Causativos {causativos(line)}')


def main():
    file = open("files/conversaciones.txt", "r")
    # file = open("conversaciones.txt", "r")  # todo: ticademia version
    opositivos_causativos(file)

    file.close()


main()
