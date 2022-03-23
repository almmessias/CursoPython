maior = menor = 0
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
    if valores[cont] > maior:
        maior = valores[cont]
        pos = cont
    for v in valores:
        print

print (f'A lista de valores é {valores}')
print (f'O maior valor digitado foi {maior} nas posições {pos}')
print (f'O menor valor digitado foi {min(valores)} nas posições')
