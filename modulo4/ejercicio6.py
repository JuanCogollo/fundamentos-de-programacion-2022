def main():
    
    N = int(input())
    
    def multiplo_de_cual():
        if(N % 2 == 0):
            print(f'{N} es multiplo de 2')
        elif (N % 3 == 0):
            print(f'{N} es multiplo de 3')
        elif (N % 5 == 0):
            print(f'{N} es multiplo de 5')
        elif (N % 7 == 0):
            print(f'{N} es multiplo de 7')
        else:
            print(f'{N} no es multiplo de ninguno de los primeros cuatro primos')
            
    
    multiplo_de_cual()
            
if (__name__ == '__main__'):
    main()