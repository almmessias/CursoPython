
from itertools import count


n = str(input ('Digite seu nome completo: ')).strip()

print (n.upper())
print (n.lower())
dividido = n.split()
print (len (n) - n.count(' '))
print (len (dividido[0]))
