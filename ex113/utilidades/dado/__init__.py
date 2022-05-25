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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mValor inválido, tente novamente.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[031mUsuário preferiu não digitar nenhum número\033[m')
            return 0
        else:
            return num
