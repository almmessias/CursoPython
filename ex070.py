print ('Lojas Luiza')
print ('+' * 40)
stotal = cproduto = barato = cont = 0
nproduto = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input ('Digite o preço do produto: R$'))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if preco > 1000:
        cproduto += 1
    stotal += preco
    cont += 1
    if cont == 1:
        barato = preco
        nproduto = nome
    else:
        if preco < barato:
            barato = preco
            nproduto = nome
    print ('=' * 40)
    if continua == 'N':
        print ('=' * 40)
        print ('Compras finalizada')
        break
print (f'O total das compras foi R${stotal:.2f}')
print (f'Teve {cproduto} acima de R$1.000.')
print (f'O produto mais barato foi {nproduto} custando R${barato:2f}.')
