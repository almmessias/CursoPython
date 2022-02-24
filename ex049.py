num = int (input ('Digite um número para tabuada: '))
for c in range (0, 11):
    print ('{} * {:2} = {}'.format(num, c, num * c))
