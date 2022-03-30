num = []
while True:
    valor = (int (input ('Digite um valor: ')))
    if valor not in num:
        print ('Valor adicionado com sucesso')
        num.append(valor)
    else:
        print ('Valor duplicado, não vou adicionar.')
    opcao = str (input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print (sorted(num))
