'''exp = str(input ('Digite uma expressão: '))
if exp.count('(') == exp.count(')'):
    print ('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
'''
expr = str (input ('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
print (pilha)
if len(pilha) == 0:
    print ('Sua expressão está válida')
else:
    print ('Sua expressão está inválida')
