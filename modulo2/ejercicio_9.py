# Un tanque de agua tiene una forma perfectamente cilíndrica. Si inicialmente está
# completamente lleno y empieza a vaciarse a una tasa de v metros cúbicos por minuto,
# ¿Cuál será su volumen después de m minutos? El volumen inicial no lo conocemos, pero
# si su radio r y su altura h (ambos expresados en metros).
import math

pi = math.pi
r = float(input())
h = float(input())
v = float(input())
m = float(input())

def razon_cambio(r,h,v,m):
    result = round(((pi * r**2 * h) - v * m), 3)
    return result

result =razon_cambio(r,h,v,m)
if result >= 0:
    print(result)
else:
    print(0)



