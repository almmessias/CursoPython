valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]   
print (f'A lista de valores é {valores}')
print (f'O maior número {maior} aparece na posição ',end='')
for pos, v in enumerate(valores):
    if v == maior:
        print (f'{pos}...', end='')
print()
print (f'O menor número {menor} aparece na posição ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print (f'{pos}...', end='')