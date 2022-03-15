from random import randint
r = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print (f'Os valores sorteados foram {r}')
maior = menor = 0
for teste in range(0, 4):
    print (r[teste], end=' - ')
if r[0] > r[1]:
    maior = r[0]

print (f'O menor número é {menor}')
print (f'O maior número é {maior}')