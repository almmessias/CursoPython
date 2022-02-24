from random import shuffle
n1 = input ('Nome do primeiro estudante: ')
n2 = input ('Nome do segundo estudante: ')
n3 = input ('Nome do terceiro estudante: ')
n4 = input ('Nome do quarto estudante: ')

l = [n1, n2, n3, n4]
shuffle(l)
print ('A ordem de apresentação são:',l)
