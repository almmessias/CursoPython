from ex115.lib.interface import *

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Ver Pessoas Cadastradas')
    elif resposta == 2:
        cabecalho('Cadastrar Nova Pessoa')
    elif resposta == 3:
        print('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mOpção inválida, tente novamente\033[m')
