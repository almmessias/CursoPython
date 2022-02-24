soma = 0
for contagem in range (1, 7):
    num = int (input ('Digite o {} valor: '.format(contagem)))
    if num % 2 == 0:
        soma += num
print (soma)
