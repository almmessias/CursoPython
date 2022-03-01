import random
from time import sleep
r = random.randint(0, 10)
acertou = False
soma = 0
while not acertou:
    n = int (input ('Entre 1 e 10, qual foi o número escolhido pelo computador: '))
    print ('Processando...')
    print ('-=-' * 20)
    sleep(1)
    if r == n:
        acertou = True
    else:
        if r > n:
            print ('Mais... Tente novamente')
        elif r < n:
            print ('Menos... Tente novamente')
    soma += 1
print ('Você venceu! Eu pensei no número {} e vc acertou na {} vez!!!'.format(r, soma))