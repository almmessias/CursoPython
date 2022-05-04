def notas(*num, sit=False):
    '''
    -> Função para analisar notas e a situação de vários alunos.
    param num:uma ou mais notas dos alunos (aceita N notas).
    param sit: valor opcional, indicando a situação do aluno.
    return: dicionário com várias informações com as informações da turma.
    '''
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(6, 8, 9)
print (resp)
