cont = soma = num = 0
num = int (input ('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int (input ('Digite um número: '))
print ('A soma entre os número é {}.'.format(soma))
print ('Você digitou {} números.'.format(cont))
