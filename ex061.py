print ('Gerador de PA')
print ('-=-' * 10)
primeiro = int (input ('Digite o primeiro termo: '))
razao = int (input ('Digite a razão: '))
c = 0
while c <= 10:
    c += 1
    print ('{}'.format(primeiro), end=' - ')
    primeiro += razao
#print (decimo)
print ('FIM')
