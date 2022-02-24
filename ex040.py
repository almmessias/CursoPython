n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
if (n1 + n2) / 2 < 5:
    print ('Reprovado! Nota {}'.format((n1 + n2) / 2))
elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 < 7:
    print ('Recupeção! Nota {}'.format((n1 + n2) / 2))
else:
    print ('Aprovado! Nota {}'.format((n1 + n2) / 2))