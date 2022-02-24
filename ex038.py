n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número: '))
if n1 == n2:
    print ('Os números {} e {} são iguais'.format(n1, n2))
elif n1 > n2:
    print ('O primeiro número {} é maior'.format(n1))
else:
    print ('O segundo número {} é maior'.format(n2))
