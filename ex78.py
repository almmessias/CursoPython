num = []
maior = menor = 0
for c in range (0,5):
    num.append(int (input(f"Digite o valor na posição {c}: ")))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print (num)
print (f'maior {maior} menor {menor} ')
print (f'O maior número é {maior} na posição ', end='')
for i, v in enumerate(num):
    if v == maior:
        print (f'{i}...', end='')
print ()
print (f'O menor número é {menor} na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print (f'{i}...', end='')
print ()