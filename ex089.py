geral = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print (len(geral))
print ('-=' * 15)
print (f'{"No":<4}{"Nome":<10}{"Média":>6}')
print ('-' * 30)
for i, l in enumerate(geral):
    print (f'{i:<4}{l[0]:<10}{l[2]:>6.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        break
    print ('-' * 30)
    if opc <= len(geral) - 1:
        print (f'As notas de {geral[opc][0]} são {geral[opc][1]}')
print (geral)