def serieJulianachi(n):
    Julianachi = [1]
    while Julianachi[-1] <= n:
        contador = 0
        for i in range(1, Julianachi[-1]+1):
            if Julianachi[-1] % i == 0:
                contador += 1
        Julianachi.append(Julianachi[-1] + contador)
    return (Julianachi)


lista = serieJulianachi(10000)
numeros = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        numeros.append(n)
for i in numeros:
    if i in lista:
        print('Pertenece a la serie de Julianachi')
    else:
        print('No pertenece a la serie de Julianachi')
