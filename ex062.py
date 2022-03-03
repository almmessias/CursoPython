print ('Gerador de PA')
print ('-=-' * 10)
termo = int (input ('Digite o primeiro termo: '))
razao = int (input ('Digite a razão: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        c += 1
        print ('{}'.format(termo), end=' - ')
        termo += razao
    print ('Pausa')
    mais = int (input ('Quantos termos vc quer mostrar mais: '))
print ('Progressão finalizada com {} termos mostrados.'.format(total))
