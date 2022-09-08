def main():
    X = float(input())
    Y = float(input())

    if X == 0 and Y == 0:
        print(f'La coordenada ({X}, {Y}) corresponde al origen')
    elif X == 0:
        print(f'La coordenada ({X}, {Y}) esta sobre el eje Y')
    elif Y == 0:
        print(f'La coordenada ({X}, {Y}) esta sobre el eje X')
    elif X > 0 and Y > 0:  # Cuadrante 1 ( x > 0, y > 0 )
        print(f'La coordenada ({X}, {Y}) se encuentra en el cuadrante 1')
    elif X < 0 and Y > 0:  # Cuadrante 2 ( x < 0, y > 0 )
        print(f'La coordenada ({X}, {Y}) se encuentra en el cuadrante 2')
    elif X < 0 and Y < 0:  # Cuadrante 3 ( x < 0, y < 0 )
        print(f'La coordenada ({X}, {Y}) se encuentra en el cuadrante 3')
    elif X > 0 and Y < 0:  # Cuadrante 4 ( x > 0, y < 0)
        print(f'La coordenada ({X}, {Y}) se encuentra en el cuadrante 4')


if __name__ == '__main__':
    main()
