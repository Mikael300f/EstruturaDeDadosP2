# 31. Números pares até n
def numeros_pares(n):
    return list(range(0, n+1, 2))

# 32. Soma dos primeiros n números naturais
def soma_naturais(n):
    return sum(range(1, n+1))

# 33. Potências de 2 até um determinado expoente
def potencias_de_dois(exp):
    return [2**i for i in range(exp+1)]