num1 = int (input ('Digite o primeiro termo: '))
razao = int (input ('Digite a razao de uma PA: '))
decimo = num1 + (10 - 1) * razao
for c in range(num1, decimo + razao, razao):
    print ('{}'.format(c), end=' ')
