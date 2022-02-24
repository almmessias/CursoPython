viagem = int (input ('Qual a distância da viagem em km? '))
if viagem <= 200:
    print ('O custo da viagem é R${:.2f}'.format(viagem * 0.50))
else:
    print ('O custo da viagem é R${:.2f}'.format(viagem * 0.45))

# preço = distancia * 0.50 if distancia < 200 else distancia * 0.45
