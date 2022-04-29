def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    return: O valor do fatorial de um número n.
    """
    f = 1
    for a in range(n, 0, -1):
        if show == True:
            print (a, 'x ' if a != 1 else '= ', end='') 
        f *= a
    return f


#print (fatorial(4))
help(fatorial)