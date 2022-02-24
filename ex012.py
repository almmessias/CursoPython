preco = float(input ('Qual valor do produto? R$'))
desconto = preco - (preco * 5 / 100)

print ('O valor do produto é R${:.2f} com desconto de 5% fica R${:.2f}'.format(preco, desconto))
