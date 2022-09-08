def main():
    horas_refl = int(input())
    minutos_refl = int(input())

    if (horas_refl == 12 or horas_refl == 0) and (minutos_refl == 0):
        print(f'{horas_refl}:{minutos_refl}')
    elif horas_refl == 12 or horas_refl == 6:
        print(f'{horas_refl - 1}:{60 - minutos_refl}')
    elif minutos_refl > 30:
        hora_correcta = 12 - horas_refl - 1
        minutos_correctos = 60 - minutos_refl
        if hora_correcta == 0:
            hora_correcta = 12
        if minutos_correctos == 60:
            minutos_correctos = 0
        print(f'{hora_correcta}:{minutos_correctos}')
    elif minutos_refl < 30:
        hora_correcta = 12 - horas_refl
        minutos_correctos = 60 - minutos_refl
        if hora_correcta == 0:
            hora_correcta = 12
        if minutos_correctos == 60:
            minutos_correctos = 0
        print(f'{hora_correcta}:{minutos_correctos}')


if __name__ == '__main__':
    main()
