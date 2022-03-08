while True:
    cont = 0
    t = int (input ('Quer ver a tabuada de qual valor: '))
    if t < 0:
        print ('Programa da Tabuada encerrado')
        break
    while cont <= 10:
        r = t * cont
        print (f'{t} X {cont:2} = {r}')
        cont += 1
