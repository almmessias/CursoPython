pessoas = {}
geral = []
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print ('Digite apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
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

#print (f'B) A média de idade é {sidade / len(geral)}')