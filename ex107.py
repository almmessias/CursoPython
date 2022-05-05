from ex107 import moeda
from ex107.moeda import dobro, metade, aumento, desconto

n = float(input('Digite o preço:'))
print (f'O dobro de R${n:.2f} é R${moeda.dobro(n):.2f}')
print (f'A metade de R${n:.2f} é R${moeda.metade(n):.2f}')
print (f'O aumento de 10% de {n:.2f} é R${moeda.aumento(n, 10):.2f}')
print (f'O desconto de 13% de {n:.2f} é R${moeda.desconto(n, 13):.2f}')
