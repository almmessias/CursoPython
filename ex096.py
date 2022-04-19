def area(larg, comp):
    total = larg * comp
    print (f'A área desse terreno {larg}x{comp} é de {total}m².')


print (f'{"Controle de terrenos"}')
print ('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
