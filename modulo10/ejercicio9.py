def count_unique(arr):
    unique = []
    for word in arr:
        if word not in unique:
            unique.append(word)

    return len(unique)


def main():
    rock = []
    reggaeton = []

    c = int(input())
    for i in range(c):
        lyrics = input()
        lyrics = lyrics.split()
        for k in range(len(lyrics)):
            reggaeton.append(lyrics[k])

    c = int(input())
    for i in range(c):
        lyrics = input()
        lyrics = lyrics.split()
        for k in range(len(lyrics)):
            rock.append(lyrics[k])

    print(f'Reggaeton: {count_unique(reggaeton)} Rock: {count_unique(rock)}')


main()
