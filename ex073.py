brasileiro = ('Atlético Mineiro','Flamengo','Palmeiras','Fortaleza','Corinthians','Red Bull Bragantino','Fluminense','America','Atlético-GO','Santos','Ceará','Internacional','São Paulo','Athletico Paranaense','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
print ('a) Os 5 primeiro colocados são:')
for cont in range (0, 5):
    print (f'{brasileiro[cont]}')
print ('#' * 50)
print ('b) Os 5 últimos colocados são:')
for cont2 in range (15, 20):
    print (f'{brasileiro[cont2]}')
print ('#' * 50)
print (sorted(brasileiro))
print ('#' * 50)
if 'Chapecoense' in brasileiro:
    print (f'A Chapecoense está em {len(brasileiro)}ª posição')
#print (f'A Chapecoense está na {brasileiro.index("Chapecoense")+1}ª posição.')
