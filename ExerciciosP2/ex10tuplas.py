# 28. Pessoa mais velha de uma lista de tuplas
def mais_velho(pessoas):
    return max(pessoas, key=lambda pessoa: pessoa[1])

# 29. Média das coordenadas (x, y)
def media_coordenadas(coordenadas):
    x_total = sum([x for x, _ in coordenadas])
    y_total = sum([y for _, y in coordenadas])
    n = len(coordenadas)
    return (x_total / n, y_total / n)

# 30. Comprimento de cada string em uma tupla
def comprimento_strings(tupla):
    return tuple(len(s) for s in tupla)