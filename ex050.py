soma = 0
for contagem in range (0, 6):
    num = int (input ('Digite o {} valor: '.format(contagem)))
    if num % 2 == 0:
        soma += num
print (soma)
