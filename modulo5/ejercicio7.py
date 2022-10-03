# def main():
cantidad_de_lotes = int(input())
lado_del_cuadrado = float(input())
incremento = float(input())

area = 0

for i in range(cantidad_de_lotes):
    area += lado_del_cuadrado ** 2
    lado_del_cuadrado += incremento

print(f'El area total es de {area} metros cuadrados')


# if __name__ == '__main__':
#     main()
