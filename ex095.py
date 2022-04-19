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
print (f'{"cod":<3} ', end='')
for j in jogador.keys():
    print (f'{j:<5}' , end='    ')
print ()
print ('-' * 60)
for k, j in enumerate(dados):
    print (f' {k:<3}{j["nome"]:<8}{str(j["gols"]):<9}{j["total"]:>3}')
print ('-=' * 30)
while True:
    jogado = int(input('Mostrar dados de qual jogador? 999 Interrompe '))
    if jogado == 999:
        break
    elif jogado > len(dados) -1:
        print ('Não existe esse código, tente novamente ')
    else:
        print ('-' * 60)
        print (f'Levantamento do JOGADOR {dados[jogado]["nome"]}')
        for i, v in enumerate(dados[jogado]['gols']):
            print (f'No jogo {i+1}, fez {v} gols.')
print ('<< Volte Sempre >>')
print (dados)