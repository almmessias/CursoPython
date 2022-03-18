tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
        'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
        'dezoito', 'dezenove', 'vinte')
while True:
    num = int (input ('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        print('Tente novamente.', end=' ')
        num = int (input ('Digite um número entre 0 e 20: '))
    print (tupla[num])
    continua = str(input ('Quer continuar? S/N ')).strip().upper()[0]
    if continua == 'N':
        break
