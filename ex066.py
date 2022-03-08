cont = soma = 0
while True:
    num = int (input ('Digite um numero: [Digite 999 para parar] '))
    if num == 999:
        print ('FIM!')
        break
    soma += num
    cont +=1
media = soma / cont
print (f'Foram digitados {cont} números.')
print (f'A soma entre os número é {soma}')
print (f'A média entre os números é {media}')
