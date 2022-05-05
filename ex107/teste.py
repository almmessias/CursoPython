from moeda import dobro, aumento, metade, desconto

n = float(input('Digite o preço:'))
print (f'O dobro de R${n:.2f} é R${dobro(n):.2f}')
print (f'A metade de R${n:.2f} é R${metade(n):.2f}')
print (f'O aumento de 10% de {n:.2f} é R${aumento(n, 10):.2f}')
print (f'O desconto de 13% de {n:.2f} é R${desconto(n, 13):.2f}')
