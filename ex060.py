soma = 1
resultado = 0
n = int (input ('Digite um número e encontre seu fatorial: '))
for fatorial in range(n, 0, -1):
    soma = n * (n -1)
    print (soma)
    #print ('x{}'.format(fatorial), end='')
#print ('\n', resultado)
#print ('A soma do fatorial de {}! é {}'.format(n, soma))