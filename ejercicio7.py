def main():
    stopper = 1
    racimos = []

    while stopper != 0:
        stopper = int(input())
        if stopper != 0:
            racimos.append(stopper)

    uvas = []

    for racimo in racimos:
        # para cada racimo en la lista crea un contador
        # inicializado en 0
        counter = 0
        for i in range(racimo):
            # toma cada una de las uvas y ve creando una piramide
            uvas.append(i + 1)
            # y sumale 1 al counter por cada uva añadida a la pirámide
            counter += i + 1
            if counter == racimo:  # comprueba si usamos todas las uvas para la pirámide
                print('Puede ser un racimo ideal')
                break
            elif counter > racimo:
                # Si el contador se pasa sin encontrar la coincidencia, no pudo ser formada la pirámide
                print('No puede ser un racimo ideal')
                break


if __name__ == '__main__':
    main()
