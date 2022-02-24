import random
n1 = input ('Qual seu nome estudante1: ')
n2 = input ('Qual seu nome estudante2: ')
n3 = input ('Qual seu nome estudante3: ')
n4 = input ('Qual seu nome estudante4: ')
l = [n1, n2, n3, n4]
e = random.choice(l)
print ('O escolhido foi {}'.format(e))