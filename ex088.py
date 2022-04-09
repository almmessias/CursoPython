from random import randint
from time import sleep
sorteio = []
jogo = []
print ('-' *30)
print ('JOGOS DA MEGA SENA')
print ('-' *30)
jogos = int (input('Quantos jogos serão jogados? '))
print (f'SORTEANDO {jogos} JOGOS')
for c in range (0, jogos):
    for j in range (0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    sorteio.append(jogo[:])
    jogo.sort()
    print (f'Jogo {c + 1}: {jogo}')
    sleep(2)
    jogo.clear()
print (f'-=' * 5,'BOA SORTE!', '-=' * 5)
