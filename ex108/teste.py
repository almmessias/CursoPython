import moeda

n = float(input('Digite o preço: R$'))
print (f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print (f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print (f'O aumento de 10% de {moeda.moeda(n)} é {moeda.moeda(moeda.aumento(n, 10))}')
print (f'O desconto de 13% de {moeda.moeda(n)} é {moeda.moeda(moeda.desconto(n, 13))}')
