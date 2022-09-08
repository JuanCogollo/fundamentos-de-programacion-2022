# https://datagy.io/python-get-dictionary-key-with-max-value/#:~:text=The%20simplest%20way%20to%20get,maximum%20value%20of%20any%20iterable.

def main():
    how_many_players = int(input())
    how_many_games = int(input())

    players = {}
    games_results = []

    for i in range(how_many_games):
        winner_id = int(input())
        games_results.append(winner_id)

    for i in range(how_many_players):
        players[i + 1] = games_results.count(i + 1)

    print(f'Players: {players}')


if __name__ == '__main__':
    main()
