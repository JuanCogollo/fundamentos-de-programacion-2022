def main():
    how_many_soldiers = int(input())

    team_1 = []
    team_2 = []

    alive_soldiers = 0

    for i in range(how_many_soldiers):
        height = int(input())
        team_1.append(height)
        alive_soldiers += 1

    for i in range(how_many_soldiers):
        height = int(input())
        team_2.append(height)
        alive_soldiers += 1

    team_1.sort()
    team_2.sort(reverse=True)

    for i in range(how_many_soldiers):
        if (team_1[i] % 2 == 0 and team_2[i] % 2 == 0) or (team_1[i] % 2 != 0 and team_2[i] % 2 != 0):
            alive_soldiers -= 2

    print(f'Sobreviven {alive_soldiers} soldados')


if __name__ == '__main__':
    main()
