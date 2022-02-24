r1 = float (input ('Primeiro lado: '))
r2 = float (input ('Segundo lado: '))
r3 = float (input ('Terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os lados acima podem formar um triangulo')
    if r1 == r2 == r3:
        print ('O triângulo é um Equilátero: todos os lado são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print ('O triângulo é um Isósceles: dois lados iguais')
    elif r1 != r2 != r3 != r1:
        print ('O triângulo é um Escaleno: todos os lados diferentes')
else:
    print ('Os lados não formam um triângulo')
