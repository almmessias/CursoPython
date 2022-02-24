maior = 0
#menor = 100
for contagem in range (0, 5):
    peso = float (input ('Qual seu peso: (Kg) '))
    if peso > maior:
        maior = peso
print (maior)
