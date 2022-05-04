def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('Erro, digite um valor válido')
        if ok:
           break
    return valor
    
num = LeiaInt('Digite um número: ')
print (f'Você digitou o número {num}')
