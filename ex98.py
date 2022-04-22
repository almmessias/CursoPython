from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = +(passo)
    if inicio > fim:
        passo = -(passo)
    if passo > 0:
        for i in range (inicio, fim+1, passo):
            print (i, end=" ")
    elif passo < 0:
        for i in range (inicio, fim, passo):
            print (i, end=" ")
    print ('FIM!')


print ('-=' * 30)
print ('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print ('-=' * 30)
print ('Contagem de 10 até 0 de 2 em 2')
contador (10, 0, 2)
print ('-=' * 30)
print ('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
print ('-=' * 30)
print (f'Contagem de {ini} até {fi} de {pas} em {pas}')
contador (ini, fi, pas)
