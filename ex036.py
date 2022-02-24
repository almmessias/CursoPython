valor = float (input ('Qual é o valor do imóvel? R$'))
salario = float (input ('Qual é o salário? R$'))
anos = int (input ('Em quantos anos ele vai pagar o imóvel? '))
parcela = valor / (anos * 12)
aprova = salario * 30 / 100
if aprova < parcela:
    print ('Não aprovado! Valor da parcela R${:.2f} excedeu 30% da renda R${:.2f}.'.format(parcela, aprova))
else:
    print ('Aprovado! Valor da parcela será de {:.2f}'.format(parcela))
