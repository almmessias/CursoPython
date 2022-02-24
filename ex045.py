from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print ('-=-' * 10)
jogador = int (input ('''Vamos jogar JOKENPÔ:
0 - Pedra
1 - Papel
2 - Tesoura
Escolha uma das opções: '''))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO')
sleep(1)
if computador == 0:
    if jogador == 0:
        print ('Empatou')
    elif jogador == 1:
        print ('Jogador venceu')
    elif jogador == 2:
        print ('Computador venceu')
    else:
        print ('Opção inválida')
elif computador == 1:
    if jogador == 0:
        print ('Computador venceu')
    elif jogador == 1:
        print ('Empate')
    elif jogador == 2:
        print ('Jogador venceu')
    else:
        print ('Opção inválida')
elif computador == 2:
    if jogador == 0:
        print ('Jogador venceu')
    elif jogador == 1:
        print ('Computador venceu')
    elif jogador == 2:
        print ('Empate')
    else:
        print ('Opção inválida')
print ('-=-' * 10)
print ('Computador jogou {}'.format(itens[computador]))
print ('Jogador jogou {}'.format(itens[jogador]))
