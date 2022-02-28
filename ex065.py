loop = 1
soma = 0
repeat = 0
while loop != 0:
    num = int (input ('Digite um número: '))
    loop = str(input ('Você quer continuar? S/N ')).lower
    soma = soma + num
    repeat + 1
    if loop == 'n':
        loop = 0
        print ('Fim')
print ('A média entre os número digitados é {}'.format(soma / repeat))
