from datetime import date
maior = 0
menor = 0
for contador in range (0, 7):
    nasc = int (input ('Digite seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1

print ('{} pessoas já atingiram a maior idade'.format(maior))
print ('{} pesssoas ainda não atingiram a maior idade'.format(menor))
