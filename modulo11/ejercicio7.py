from random import randint


def judge(human, robot):
    results = {
        "human": 0,
        "robot": 0
    }
    for i in range(10):
        if human[i] > robot[i]:
            results["human"] += 1
        elif human[i] < robot[i]:
            results["robot"] += 1

    return results


def generate_cards():
    cards = []
    for i in range(10):
        cards.append(randint(1, 13))
    return cards


def main():
    c = int(input())
    for i in range(c):
        d = input()
        d = d.split(" ")[1:]
        d = list(map(lambda x: int(x), d))
        res = judge(generate_cards(), d)
        print(f"Puntos humano: {res['human']} Puntos plataforma: {res['robot']}")


main()
