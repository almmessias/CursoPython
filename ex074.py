from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print (f'Os valores sorteados foram: ', end='')
for n in num:
    print (f'{n} ', end='')
print (f'\nO menor número é {max(num)}')
print (f'O maior número é {min(num)}')
