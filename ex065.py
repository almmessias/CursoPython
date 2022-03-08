resp = 'S'
soma = media = maior = menor = 0
while resp == 'S':
    num = int (input ('Digite um número: '))
    soma += num
    media += 1
    if media == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str (input ('Quer continuar? S/N ')).upper().strip()[0]
media = soma / media
print ('A soma foi {}'.format(soma))
print ('A média foi {:.2f}'.format(media))
print ('O maior num é {} e o menor é {}'.format(maior, menor))
