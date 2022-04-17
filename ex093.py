sgol = 0
gol = []
jogador = {}
jogador["nome"] = str(input('Nome: '))
partidas = int(input('Partidas: '))
for p in range(0, partidas):
    gols = int(input(f'Gols partida {p+1}: '))
    gol.append(gols)
    sgol += gols
jogador["gols"] = gol
jogador["total"] = sgol
print ('-=' * 30)
print (jogador)
print ('-=' * 30)
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print ('-=' * 30)
print (f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gol):
    print (f'   => Na partida {i+1}, fez {v} gols')
print (f'Foi um total de {jogador["total"]} gols')
