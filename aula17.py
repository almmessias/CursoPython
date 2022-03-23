valores = []
for c in range(0, 2):
    valores.append(int(input('Digite um valor: ')))
print (valores)
print (c)
for c, v in enumerate(valores):
    print (f'Na posição {c} eu encontrei o valor {v}!')
print (enumerate(valores))