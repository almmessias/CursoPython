a = 0
b = 0
c = 0
while True:
    idade = int(input ('Digite sua idade: '))
    sexo = str(input ('Digite seu sexo: M/F ')).upper().strip()[0]
    if sexo not in 'MF':
        sexo = str(input ('Digite seu sexo: M/F ')).upper().strip()[0]
    continua = str(input ('Você quer continuar? S/N ')).upper().strip()[0]
    if continua not in 'SN':
        continua = str(input ('Você quer continuar? S/N ')).upper().strip()[0]
    if idade >= 18:
        a += 1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade < 20:
        c += 1
    if continua == 'N':
        break
print (f'{a} pessoas tem mais de 18 anos.')
print (f'{b} homens cadastrados.')
print (f'{c} mulheres com menos de 20 anos')
