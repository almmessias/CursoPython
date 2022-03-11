tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int (input ('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int (input ('Tente novamente, digite um número entre 0 e 20: '))
print (tupla[num])
