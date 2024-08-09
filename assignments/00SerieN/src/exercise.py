def main():
    #escribe tu código abajo de esta línea
    n = int(input('Dame el valor de n:'))

    for i in range(1,n+1):
        print(i, end=', ')

    for i in range(n-1,0,-1):
        if i != 1:
            print(i, end=', ')
        else:
            print(i)

if __name__=='__main__':
    main()
