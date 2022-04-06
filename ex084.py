dado = []
geral = []
maior = menor = 0
while True:
    dado.append(str(input('Insira o nome: ')))
    dado.append(int(input('Insira o peso: ')))
    if len(geral) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    geral.append(dado[:])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    dado.clear()
    if resp == "N":
        break
print (geral, dado)
print (f'Foram cadastradas {len(geral)} pessoas')
print (f'O maior peso foi {maior}Kg, peso de ', end='')
for p in geral:
    if p[1] == maior:
        print (f'{p[0]}... ', end='')
print ()
print (f'O menor peso foi {menor}Kg, peso de ', end='')
for p in geral:
    if p[1] == menor:
        print (f'{p[0]}... ', end='')
