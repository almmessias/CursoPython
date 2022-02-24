num = int (input ('Digite um número inteiro: '))
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print ('{} é um número primo'.format(num))
else:
    print ('{} não é um número primo.'.format(num))
