def msg(val, cal):
    print(f'El porcentaje {val} corresponde a la calificacion {cal}')

def main():

    X = float(input())

    if (X >= 90):
        msg(X, 'A')
        print(f'El porcentaje {X} corresponde a la calificacion A')
    elif (X >= 80 and X < 90):
        print(f'El porcentaje {X} corresponde a la calificacion B')
    elif (X >= 70 and X < 80):
        print(f'El porcentaje {X} corresponde a la calificacion C')
    elif (X >= 60 and X < 70):
        print(f'El porcentaje {X} corresponde a la calificacion D')
    elif (X >= 40 and X < 60):
        print(f'El porcentaje {X} corresponde a la calificacion E')
    else:
        print(f'El porcentaje {X} corresponde a la calificacion F')

if (__name__ == '__main__'):
    main()