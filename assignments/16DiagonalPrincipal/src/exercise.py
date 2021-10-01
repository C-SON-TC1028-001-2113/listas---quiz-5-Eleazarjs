
def main():
    u = int(input())
    o = int(input())
    p = u*o
    lista1=[]
    lista2=[]
    index=0
    if u==o:
        for i in range (p):
            l=int(input())
            lista1.append(l)
        while index <p:
            e=lista1[index]
            lista2.append(e)
            index=index+(u+1)
        print(lista2)
    else:
        print('La matriz no es cuadrada')
if __name__=='__main__':
    main()
