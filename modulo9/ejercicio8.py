def encrypt(file):
    encrypted_file = ''
    for line in file:
        line = line.replace('\n', '')
        for i in range(len(line)):
            encrypted_file += line[-1 - i]
        encrypted_file += '\n'

    return encrypted_file


def main():
    # file = open("files/mensaje.txt", "r")
    file = open("mensaje.txt", "r")  # todo: ticademia version

    print(encrypt(file))

    file.close()


main()
