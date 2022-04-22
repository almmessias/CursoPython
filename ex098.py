from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1    
    print ('-=' * 30)
    print (f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        while i <= f:
            print (i, end=' ', flush=True)
            sleep(0.2)
            i += p
    else:
        while i >= f:
            print (i, end=' ', flush=True)
            sleep(0.2)
            i -= p
    print ('FIM')


contador(0, 10, 1)
contador(10, 0, 2)
print ('-=' * 30)
print ('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

