def main():
    
    quantityWanted = int(input())

    if (quantityWanted >= 50000):
        _50 = quantityWanted // 50000
        quantityWanted -= 50000 * _50
        print(f'{_50} de $50000')
    if (quantityWanted >= 20000):
        _20 = quantityWanted // 20000
        quantityWanted -= 20000 * _20
        print(f'{_20} de $20000')
    if (quantityWanted >= 10000):
        _10 = quantityWanted // 10000
        quantityWanted -= 10000 * _10
        print(f'{_10} de $10000')
    if (quantityWanted >= 5000):
        _5 = quantityWanted // 5000
        quantityWanted -= 5000 * _5
        print(f'{_5} de $5000')
    if (quantityWanted >= 2000):
        _2 = quantityWanted // 2000
        quantityWanted -= 2000 * _2
        print(f'{_2} de $2000')
    if (quantityWanted >= 1000):
        _1 = quantityWanted // 1000
        quantityWanted -= 1000 * _1
        print(f'{_1} de $1000')
    
if (__name__ == '__main__'):
    main()