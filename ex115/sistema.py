from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção 1 - Ver pessoas cadastradas
        #cabecalho('Ver Pessoas Cadastradas')
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar nova pessoa
        cabecalho('Cadastrar Nova Pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mOpção inválida, tente novamente\033[m')
