print ('''Qual seu sexo:
    M - Masculino
    F - Feminino''')
sexo = str(input ('Escolha uma opção: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str (input ('Valor incorreto, informe seu sexo: M/F ')).upper().strip()[0]
print ('Sexo {} registrado com sucesso'.format(sexo))
