def escreva(msg):
    tam = len(msg) + 2
    print ('~' * tam)
    print (f' {msg}')
    print ('~' * tam)


msg = str(input('Digite uma msg: '))
escreva(msg)
