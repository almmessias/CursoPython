salario = float (input ('Digite seu salário: R$'))
if salario > 1250:
    print ('Seu salário com aumento ficou R${:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print ('Seu salário com aumento ficou R${:.2f}'.format(salario + (salario * 15 / 100)))
