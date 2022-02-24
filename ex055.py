maior = 0
menor = 0
for contagem in range (1, 6):
    peso = float (input ('Qual peso da {}ª pessoa: (Kg) '.format(contagem)))
    if contagem == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ('O maior peso é {}'.format(maior))
print ('O menor peso é {}'.format(menor))