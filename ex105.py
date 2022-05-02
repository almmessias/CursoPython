def notas(*num, sit=False):
    soma = media = cont = maior = menor = 0
    tot = len(num)
    for c in num:
        if cont == 0:
            maior = menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        cont += 1
        soma += c
    media = soma / len(num)
    dic = {"total":tot,"Maior":maior,"Menor":menor,"Média":media}
    if sit == True:
        if media <= 5:
            situacao = 'Ruim'
        elif 5 < media < 7:
            situacao = 'Razoável'
        else:
            situacao = 'Boa'
        dic = {"total":tot,"Maior":maior,"Menor":menor,"Média":media,"Situação":situacao}
    return dic


resp = notas(7, 10, 8)
print (resp)