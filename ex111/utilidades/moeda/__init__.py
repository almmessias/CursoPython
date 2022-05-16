def resumo(num, aument=0, descont=0):
    print('=' * 44)
    print(f'{"Resumo do valor":^44}')
    print('=' * 44)
    print(f'Preço Analisado: \t{moeda(num):>20}')
    print(f'Dobro do preço: \t{dobro(num, True):>20}')
    print(f'Metade do preço: \t{metade(num, True):>20}')
    print(f'{aument}% de aumento: \t{aumento(num, aument, True):>20}')
    print(f'{descont}% de desconto: \t{desconto(num, descont, True):>20}')


def metade(num, formato=False):
    resp = num / 2
    return resp if formato is False else moeda(resp)


def dobro(num, formato=False):
    resp = num * 2
    return resp if not formato else moeda(resp)


def aumento(num, tax, formato=False):
    resp = num + (num * tax / 100)
    return resp if formato is False else moeda(resp)


def desconto(num, tax, formato=False):
    resp = num - (num * tax / 100)
    return resp if formato is False else moeda(resp)


def moeda(num, cifrao='R$'):
    return f'{cifrao}{num:>.2f}'.replace('.', ',')
