from datetime import date
ano = int (input ('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print ('Sua idade {}, Até 9 anos: Mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print ('Sua idade {}, Até 14 anos: Infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print ('Sua idade {}, Até 19 anos: Junior'.format(idade))
elif  idade == 20:
    print ('Sua idade {}, Até 20 anos: Sênior'.format(idade))
else:
    print ('Sua idade {}, Acima de 20 anos: Master'.format(idade))