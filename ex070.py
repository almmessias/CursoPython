print ('Lojas Luiza')
print ('+' * 40)
stotal = cproduto = barato = 0
nproduto = 'nenhum'
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input ('Digite o preço do produto: R$'))
    continua = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if continua not in 'SN':
        continua = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if preco > 1000:
        cproduto += 1
    stotal += preco
    print ('=' * 40)
    if continua == 'N':
        print ('=' * 40)
        print ('Compras finalizada')
        break
print (f'O total das compras foi R${stotal:.2f}')
print (f'Teve {cproduto} acima de R$1.000.')
print (f'O produto mais barato foi {nproduto} custando R${barato}.')
