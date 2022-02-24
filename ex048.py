soma = 0
for contador in range (1, 501, 2):
    if contador % 2 == 1:
        #print ('Impares {}'.format(contador))
        if contador % 3 == 0:
            #print ('Multiplos de 3 que sejam impares {}'.format(contador))
            soma = soma + contador
print ('A soma entre os números ímpares múltiplos de 3 é: {} '.format(soma))
