from random import randint
def sorteia(lista):
    print ('Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print (n, end=' ')
    print('FIM')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print (f'Somandos os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)