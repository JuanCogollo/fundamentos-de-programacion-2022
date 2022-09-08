# Doña Gloria tiene una parcela de forma perfectamente rectangular. La quiere vender,
# pero no conoce su área, lo que sí sabe es que uno de los lados del terreno mide X metros
# y la diagonal mide Y metros

from math import sqrt

area = None 
catetoConocido = float(input()) 
hipotenusa = float(input())

catetoDesc = sqrt(hipotenusa**2 - catetoConocido**2)
areaRect = round(catetoConocido * catetoDesc, 2)

print(f'El area total es de {areaRect} metros cuadrados')
