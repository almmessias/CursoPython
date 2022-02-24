velocidade = float (input ('Qual é a velocidade do carro? '))
if velocidade > 80:
    print ('Você foi multado, valor da multa é R${}'.format((velocidade-80)*7))
print ('Dirija com segurança!')
