import random
from time import sleep

r = random.randint(0,5)
n = int (input ('Entre 1 e 5, qual foi o número escolhido pelo computador: '))
print ('Processando...')
print ('-=-' * 20)
sleep(2)
if r == n:
    print ('Você venceu! Eu pensei no número {} e vc acertou!!!'.format(r))
else:
    print ('Você perdeu. Eu pensei no número {}!'.format(r))
