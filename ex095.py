dados = []
gol = []
jogador = {}
while True:
    gol.clear()
    jogador.clear()
    jogador["nome"] = str(input('Nome: '))
    partidas = int(input('Partidas: '))
    for p in range(0, partidas):
        gol.append(int(input(f'Gols partida {p+1}: ')))
    jogador["gols"] = gol[:]
    jogador["total"] = sum(gol)
    dados.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print ('-=' * 30)
print (f'{"Cod":<2}{"Nome":^8}{"Gols":<5}{"Total":>3}')
print ('-' * 30)
for k, v in jogador.items():
    print (f'{k}{v["Nome"]}{v["Gols"]}{v["Total"]}')
'''print (jogador)
print ('-=' * 30)
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print ('-=' * 30)
print (f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gol):
    print (f'   => Na partida {i+1}, fez {v} gols')
print (f'Foi um total de {jogador["total"]} gols')'''
