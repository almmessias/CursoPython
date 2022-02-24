n = int ( input ('Digite um número inteiro: '))
print ('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int (input ('Escolha sua opção: '))
if opcao == 1:
    print ('{} Convertido para BINARIO é igual a {}'.format(n, bin(n)[:2]))
elif opcao == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[:2]))
elif opcao == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[:2]))
else:
    print ('Opção errada, selecione: \n1 para BINARIO \n2 para OCTAL \n3 para HEXADECIMAL')
