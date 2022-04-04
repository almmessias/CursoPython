'''lista = []
par = []
impar = []
while True:
    n = int (input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str (input('Tente novamente, quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print (f'A lista inteira é: {lista}')
print (f'A lista par é: {par}')
print (f'A lista impar é: {impar}')
'''
lista = []
pares = []
impares = []
while True:
    lista.append(int (input('Digite um valor: ')))
    resp = str (input('Tente novamente, quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print (f'A lista inteira é: {lista}')
print (f'A lista par é: {pares}')
print (f'A lista impar é: {impares}')
