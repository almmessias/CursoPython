def metade(num):
    resp = num / 2
    return resp
    
def dobro(num):
    resp = num * 2
    return resp

def aumento(num, tax):
    resp = num + (num * tax / 100)
    return resp

def desconto(num, tax):
    resp = num - (num * tax / 100)
    return resp


def moeda(num, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.',',')
