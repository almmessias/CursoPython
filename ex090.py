dicionario = {}
dicionario["nome"] = str(input('Nome: '))
dicionario["media"] = float(input('Média: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
elif dicionario['media'] >= 5:
    dicionario['situacao'] = 'Recuperação'
else:
    dicionario['situacao'] = 'Reprovado'
print ('-=' * 20)
for k, v in dicionario.items():
    print (f'- {k} é igual a {v}')
