import math
a = float(input ('Qual é o angulo? '))

print ('O angulo é {}\nO seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(a, math.cos(math.radians(a)), math.sin(math.radians(a)), math.tan(math.radians(a))))
