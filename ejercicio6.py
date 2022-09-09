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

    most_winners = [key for key, value in players.items() if value == max(players.values())]

    for winner in most_winners:
        print(winner)


if __name__ == '__main__':
    main()
