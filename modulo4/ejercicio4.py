def faltan_x_to_12(how_many):
    print(f'Faltan {str(how_many)} para las 12')


def main():
    hora = int(input())
    minutos = int(input())
    periodo = str(input())

    if hora == 12 and minutos == 0 and periodo == 'pm':
        faltan_x_to_12('720')
    elif hora == 12 and minutos == 0 and periodo == 'am':
        faltan_x_to_12('1440')
    elif periodo == 'pm' and hora != 12:
        rest_day = 720  # al dia le quedan 720 minutos
        total_mins = hora * 60 + minutos
        to_twelve = rest_day - total_mins
        faltan_x_to_12(to_twelve)
    elif periodo == 'pm' and hora == 12:
        rest_day = 720
        to_twelve = rest_day - minutos
        faltan_x_to_12(to_twelve)
    elif periodo == 'am' and hora != 12:
        rest_day = 1440  # al dia le quedan 1440 minutos
        total_mins = hora * 60 + minutos
        to_twelve = rest_day - total_mins
        faltan_x_to_12(to_twelve)
    elif periodo == 'am' and hora == 12:
        rest_day = 1440
        to_twelve = rest_day - minutos
        faltan_x_to_12(to_twelve)


if __name__ == '__main__':
    main()
