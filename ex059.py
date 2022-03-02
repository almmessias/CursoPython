print ('Calculadora')
n1 = float (input ('Digite o primeiro valor: '))
n2 = float (input ('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print ('''Suas opções são:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int (input ('Escolha uma opção: '))
    if opcao == 1:
        resultado = n1 + n2
        print ('{} + {} = {}'.format(n1, n2, resultado))
    elif opcao == 2:
        resultado = n1 * n2
        print ('{} * {} = {}'.format(n1, n2, resultado))
    elif opcao == 3:
        if n1 > n2:
            print ('O primeiro valor é maior {}'.format(n1))
        else:
            print ('O segundo valor é maior {}'.format(n2))
    elif opcao == 4:
        n1 = float (input ('Digite o primeiro valor: '))
        n2 = float (input ('Digite o segundo valor: '))
    elif opcao == 5:
        print ('FIM')
    else:
        print ('Opção inválida! Escolha novamente')
print ('Fim do programa!')
