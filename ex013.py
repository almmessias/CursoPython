salario = float(input ('Qual seu salário: R$'))
aumento = salario + (salario * 15 / 100)

print ('Seu salário é R${:.2f} com 15% de aumento ficará R${:.2f}'.format(salario,aumento))