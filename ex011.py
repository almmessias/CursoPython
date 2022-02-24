l = float(input ('Digite a largura da parede: '))
a = float(input ('Digite a altura da parede: '))
area = l * a

t = 2

print ('A área em m2 da parede é {}'.format(area))
print ('Você precisará de {:.1f} litros de tinta para pintar essa parede'.format(area/t))
