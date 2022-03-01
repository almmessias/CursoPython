loop = 1
soma = 0
repeat = 0
maior = 0
while loop != 0:
    num = int (input ('Digite um número: '))
    loop = str(input ('Você quer continuar? S/N ')).lower()
    soma = soma + num
    menor = num
    repeat += 1
    if loop == 'n':
        loop = 0
        print ('Fim')
    if menor < num:
        menor = num
    if num > maior:
        maior = num
print ('A média entre os número digitados é {}'.format(soma / repeat))
print ('O menor número digitado foi {} e o maior foi {}.'.format(menor, maior))
print (repeat)
