print ('{:=^40}'.format('Lojas Messias'))
valor = float (input ('Qual valor das compras: R$'))
print ('''Qual é a condição de pagamento?
1 - Dinheiro/Cheque
2 - Cartão
3 - 2x no Cartão
4 - 3x no Cartão''')
pagamento = int (input ('Seleciona uma forma de pagamento: '))
if pagamento == 1:
    print ('Pagamento em dinheiro ou cheque, desconto de 10%, valor é R${:.2f} com desconto ficará R${:.2f}'.format(valor, valor - (valor * 10 / 100)))
elif pagamento == 2:
    print ('Pagamento no cartão a vista, desconto de 5%, valor é R${:.2f} com desconto ficará R${:.2f}'.format(valor, valor - (valor * 5 / 100)))
elif pagamento == 3:
    print ('Pagamento no cartão em 2x, valor normal R${:.2f}'.format(valor))
else:
    print ('Pagamento no cartão em 3x, acréscimo de 20% de juros, valor é R${:.2f} com acréscimo ficará R${:.2f}'.format(valor, valor + (valor * 20 / 100)))