print ('{:-^40}'.format(' BANCO ALM '))
print ('*' * 40)
saque = int (input ('Qual valor você quer sacar: R$'))
cedula = 50
total = saque
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print (f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
