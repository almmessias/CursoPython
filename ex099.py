from time import sleep
def maior(* num):
    cont = 0
    print ('Analisando os valores passados...')
    sleep(1)
    for n in num:
        print (n, end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print (f'Foram informados {cont} valores ao todo.')
    print (f'O maior valor informado foi {maior}')
    print ('-=' * 30)


maior(6, 9, 3)
maior(8, 2, 2, 1, 3)
maior(5)
