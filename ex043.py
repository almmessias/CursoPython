peso = float (input ('Qual é o peso em kilos kg? '))
altura = float (input ('Qual é a altura em metros m? '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print ('Abaixo do peso, IMC {:.2f}'.format(imc))
elif 18.5 <= imc <= 25:
    print ('Peso ideal, IMC {:.2f}'.format(imc))
elif 25 <= imc <= 30:
    print ('Sobrepeso, IMC {:.2f}'.format(imc))
elif 30 <= imc <= 40:
    print ('Obesidade, IMC {:.2f}'.format(imc))
else:
    print ('Obesidade mórbida, IMC {:.2f}'.format(imc))
