def resumo(num, aument=0, descont=0):
    print ('=' * 44)
    print (f'{"Resumo do valor":^44}')
    print ('=' * 44)
    print (f'{"Preço Analisado:":<30} {moeda(num):>10}')
    print (f'{"Dobro do preço:":<30} {dobro(num, True):>10}')
    print (f'{"Metade do preço:":<30} {metade(num, True):>10}')
    print (f'{"Aumento de {aument}%:":<30} {aumento(num, aument, True):>10}')
    print (f'{"Desconto de {descont}%:":<30} {desconto(num, descont, True):>10}')


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


def moeda(num, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.',',')
