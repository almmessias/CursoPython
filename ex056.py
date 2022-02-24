midade = 0
velho = 0
mulher = 0
for pessoas in range (1, 5):
    print ('{:^}ª pessoa'.format(pessoas))
    nome = str (input ('Digite seu nome: '))
    idade = int (input ('Digite sua idade: '))
    sexo = int (input ('''Qual seu sexo? 
    1 - Masculino
    2 - Feminino: 
    Escolha uma opção: '''))
    midade += idade
    if sexo == 1 and idade > velho:
        velho = idade
        nome1 = nome
    if sexo == 2 and idade < 20:
        mulher += 1
print ('Média de idade é {}'.format(midade / 4))
print ('O homem mais velho é o {} e ele tem {} anos.'.format(nome1, velho))
print ('No grupo tem {} mulher menor que 20 anos'.format(mulher))
