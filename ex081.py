lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'N':
        break
print (f'A lista tem {len(lista)} números.')
print (lista)
lista.sort(reverse=True)
print (f'A lista em ordem descrente é: {lista}')
if 5 in lista:
    print ('O número 5 faz parte da lista')
else:
    print ('O número 5 não faz parte da lista')
