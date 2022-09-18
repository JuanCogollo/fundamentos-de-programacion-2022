personas = []

parejasganadoras = []

suma = 1995

while True:
    n = int(input())
    if n == 0:
        break
    if n not in personas:
        personas.append(n)

numero_de_personas = len(personas)

contador = 0
while contador < numero_de_personas:
    condicion = (suma - personas[contador])
    contador += 1
    if condicion in personas:
        parejasganadoras.append(condicion)
print(int(len(parejasganadoras) / 2))
