# def is_perfect(value):

# Un número entero positivo mayor a 1 se considera como “perfecto” si es igual a la suma
# de sus divisores incluyendo la unidad pero obviamente excluyéndose a sí mismo.

# Por ejemplo, 6 es un número perfecto porque sus divisores (sin incluirse) son 1, 2 y 3 que
# al sumarlos dan 6.

# ¿Harías un programa (preferiblemente incluyendo la definición de una función) para, dado
# un conjunto de valores, decir cuales son perfectos?

def main():
    values = int(input())

    for i in range(values):
        value = int(input())
        # is_perfect(value)


if __name__ == '__main__':
    main()
