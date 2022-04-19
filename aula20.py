def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 3, 1, 2, 4, 8]
dobra(valores)
print(valores)
