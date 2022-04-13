from datetime import date
ficha = dict()
ficha['nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
ficha['idade'] = date.today().year - idade
ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['ctps'] == 0:
    print ('-=' * 20)
else:
    ficha['contratacao'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = (ficha['contratacao'] + 35) - idade
    print ('-=' * 20)
for k, v in ficha.items():
    print (f'- {k} tem o valor {v}')
