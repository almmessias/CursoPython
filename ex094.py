pessoas = {}
geral = []
sidade = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print ('Digite apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    sidade += pessoas['idade']
    geral.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print ('Digite apenas S ou N')
    if resp == 'N':
        break
print ('-=' * 30)
print (f'A) Foram cadastradas {len(geral)} pessoas')
#print (geral)
media = sidade / len(geral)
print (f'B) A média de idade é {media} anos.')
print (f'C) As mulheres cadastradas foram: ', end='')
for p in geral:
    if p['sexo'] == 'F':
        print (f'{p["nome"]}...', end=' ')
print ()
print (f'D) Pessoas acima da média: ', end='')
for p in geral:
    if p['idade'] > media:
        print (f'{p["nome"]} com {p["idade"]} anos...', end='')
