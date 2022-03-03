print ('Sequencia de Fibonacci')
print ('-' * 25)
termo = int (input ('Quantos termos você quer mostrar: '))
print ('~' * 25)
cont = 3
t1 = 0
t2 = 1
print ('{} - {}'.format(t1, t2), end=' - ')
while cont <= termo:
    cont += 1
    t3 = t1 + t2
    print ('{}'.format(t3), end=' - ')
    t1 = t2
    t2 = t3
print('FIM')
