def main():
    large = int(input())
    height = int(input())
    flag = ''

    for j in range(height):
        if j == height // 2:
            trans_row = ''
            for i in range(large):
                trans_row += '+'
            flag += trans_row
        else:
            for i in range(large):
                if i == large // 2:
                    flag += '+'
                else:
                    flag += '0'
        flag += '\n'

    print(flag)


if __name__ == '__main__':
    main()
