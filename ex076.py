precos = ('Mortadela','4.20','Pao','6.75','Mostarda','8.70','Chocolate','5.30','Banana',
        '7.40','Laranja','4.40','Leite','3.80','Vinagre','3.50','Maionese','10')
print ('-' * 50)
print (f'{"Listagem de Preços":^50}')
print ('-' * 50)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print (f'{precos[pos]:.<40}', end='')
    else:
        print (f'R$ {precos[pos]:>}')
