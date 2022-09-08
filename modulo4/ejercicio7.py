def main():

    p1 = str(input())
    p2 = str(input())
    
    def ganador(p1, p2):
        if (p1 == p2):
            print('empate')
        else:
            if (p1 == 'piedra' and p2 == 'tijera'):
                print(f'{p1} vence {p2}')
            elif (p1 == 'tijera' and p2 == 'papel'):
                print(f'{p1} vence {p2}')
            elif (p1 == 'papel' and p2 == 'piedra'):
                print(f'{p1} vence {p2}')
            else:
                if (p2 == 'piedra' and p1 == 'tijera'):
                    print(f'{p2} vence {p1}')
                elif (p2 == 'tijera' and p1 == 'papel'):
                    print(f'{p2} vence {p1}')
                elif (p2 == 'papel' and p1 == 'piedra'):
                    print(f'{p2} vence {p1}')
                

    ganador(p1, p2)
    
if (__name__ == '__main__'):
    main()