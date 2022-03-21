palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO',
            'GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO',
            'PROGRAMADOR','FUTURO','NOTEBOOK','MOUSE','TOUCH')
for pos in palavras:
    print (f'\nNa palavra {pos} temos ', end='')
    for letra in pos:
        if letra in 'AEIOU':
            print (f'{letra}',end=' ')
