precio_microh = float(input())
marca_microh = input().upper()

if marca_microh == 'HACEB':
    precio_microh = precio_microh - (precio_microh * 0.07)
    if precio_microh >= 650000:
        precio_microh = precio_microh - (precio_microh * 0.15)
        print(f'El precio a pagar es: ${precio_microh}')
    else:
        print(f'El precio a pagar es: ${precio_microh}')

elif precio_microh >= 650000:
    precio_microh = precio_microh - (precio_microh * 0.15)
    print(f'El precio a pagar es: ${precio_microh}')

else:
    print(f'El precio a pagar es: ${precio_microh}')
