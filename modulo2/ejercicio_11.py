userInput = int(input())

m, s = divmod(userInput, 60)
h, m = divmod(m, 60)

print(f'{h}:{m}:{s}')
