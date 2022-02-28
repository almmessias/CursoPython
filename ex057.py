sexo = ''
while sexo != 'm' or sexo != 'f':
    print ('''Qual seu sexo:
    m - Masculino
    f - Feminino''')
    sexo = str(input ('Escolha uma opção: ')).lower()
    print (sexo)
