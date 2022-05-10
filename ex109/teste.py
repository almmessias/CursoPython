import moeda

n = float(input('Digite o preço: R$'))
print (f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print (f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print (f'O aumento de 10% de {moeda.moeda(n)} é {moeda.aumento(n, 10, True)}')
print (f'O desconto de 13% de {moeda.moeda(n)} é {moeda.desconto(n, 13, True)}')
