def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mValor inválido, tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[031mUsuário preferiu não digitar nenhum valor.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
