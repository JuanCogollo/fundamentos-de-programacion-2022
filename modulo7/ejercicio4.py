import math


def lorentz(v):
    c = 299792458  # speed of light in a vacuum
    v = v / 3.6  # km/h => m/s
    factor = (1
              /
              (math.sqrt
               (1 - ((v ** 2)
                     /
                     (c ** 2))))
              )
    return round(factor, 15)  # round to


def main():
    values_amount = int(input())

    for i in range(values_amount):
        v_ = float(input())
        print(lorentz(v_))


if __name__ == '__main__':
    main()
