# todo: fix it
def causativos(line_):
    total = 0
    palabras_causativas = ['por tanto', 'dado que', 'por consiguiente', 'asi pues', 'por ende']
    for i in range(len(palabras_causativas)):
        if line_.find(palabras_causativas[i]) != -1:
            total += 1

    return total


# todo: fix it
def opositivos(line_):
    total = 0
    palabras_opositivas = ['sin embargo', 'no obstante', 'ahora bien', 'aun asi']
    for i in range(len(palabras_opositivas)):
        if line_.find(palabras_opositivas[i]) != -1:
            total += 1

    return total


def opositivos_causativos(file):
    for line in file:
        line = line.lower()
        print(f'Opositivos {opositivos(line)} Causativos {causativos(line)}')


# todo: fix it
def main():
    file = open("files/conversaciones.txt", "r")
    # file = open("conversaciones.txt", "r")  # todo: ticademia version
    opositivos_causativos(file)

    file.close()


main()
