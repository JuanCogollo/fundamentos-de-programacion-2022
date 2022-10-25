def is_cadena(file):
    for line in file:
        is_chain = []
        words = line.split(' ')
        for i in range(1, len(words)):
            words[i] = words[i].replace('\n', '')
            curr = words[i - 1][-2:]
            next_ = words[i][:3]
            # print(f'{curr}', '-', f'{next_}')
            if curr in next_:
                is_chain.append(True)
        if len(is_chain) == len(words) - 1:
            print('cadena completa')
        else:
            print('cadena rota')


def main():
    # file = open("files/cadena.txt", "r")
    file = open("cadena.txt", "r")  # todo: ticademia version

    is_cadena(file)

    file.close()


main()
