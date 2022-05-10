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
