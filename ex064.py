loop = 0
num = 0
soma = 0
while loop != 999:
    n = int (input ('Digite um número: '))
    soma = soma + n
    num = num + 1
    if n == 999:
        loop = 999
print ('A soma entre os número é {}.'.format(soma-loop))
print ('Você digitou {} números.'.format(num-1))