from random import randint
print ('^' * 25)
print ('Vamos jogar PAR ou ÍMPAR')
print ('^' * 25)
cont = 0
while True:
    computador = randint(0, 10)
    num = int (input ('Digite um número: '))
    escolha = str(input('Escolha PAR ou IMPAR: P/I ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou IMPAR: P/I ')).upper().strip()[0]
    soma = num + computador
    if soma % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    if result == escolha:
        print ('-' * 25)
        print (f'Computador jogou {computador} e vc {num} o resultador é {soma}')
        print ('-' * 25)
        print ('Voce Ganhou!!!')
        print ('^' * 25)
        print ('Vamos jogar novamente')
        cont += 1
    else:
        print (f'Computador jogou {computador} e vc {num} o resultador é {soma}')
        print ('Você Perdeu!!!')
        print (f'Game Over! Voce venceu {cont}')
        break
