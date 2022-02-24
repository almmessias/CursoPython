km = float (input ('Quantos km rodou? '))
dia = int (input ('Quantos dias usou o carro? '))

preco = (60 * dia) + (0.15 * km)
#rodado = 0.15 * km

print ('O valor a ser pago  é R${:.2f}'.format(preco))
