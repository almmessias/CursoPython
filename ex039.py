from datetime import date
from errno import EIDRM
nasc = int (input ('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print ('Chegou sua hora vc tem {} anos'.format(idade))
elif idade < 18:
    print ('Ainda não chegou sua hora, vc tem {} anos'.format(idade))
    print ('Seu alistamento será em {}'.format(nasc + 18))
else:
    print ('Já passou seu período de alistamento, vc tem {} anos'.format(idade))
    print ('Seu alistamento foi em {}'.format(nasc + 18))