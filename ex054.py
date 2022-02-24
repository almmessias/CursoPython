from datetime import date
maior = 0
menor = 0
for contador in range (1, 8):
    nasc = int (input ('Digite seu ano de nascimento da {}ª pessoa : '.format(contador)))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1

print ('{} pessoas já atingiram a maior idade'.format(maior))
print ('{} pesssoas ainda não atingiram a maior idade'.format(menor))
