def finding_min(list):
    sorted_list = sorted(list)
    for i in sorted_list:
        print(list.index(i) + 1)


def main():

    campistas = int(input())
    campistas_lst = []

    for i in range(campistas):
        campista = float(input())
        campistas_lst.append(campista)

    finding_min(campistas_lst)


if __name__ == '__main__':
    main()
