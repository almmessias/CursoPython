import random
from time import sleep
r = random.randint(0, 10)
n = ''
soma = 0
while r != n:
    n = int (input ('Entre 1 e 10, qual foi o número escolhido pelo computador: '))
    print ('Processando...')
    print ('-=-' * 20)
    sleep(1)
    print ('Voce errou')
    soma += 1
if r == n:
    print ('Você venceu! Eu pensei no número {} e vc acertou na {} vez!!!'.format(r, soma))
'''else:
    print ('Você perdeu. Eu pensei no número {}!'.format(r))'''
