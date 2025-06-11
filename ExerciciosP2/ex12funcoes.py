# 34. Sequência de Fibonacci (recursiva)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 35. Função lambda que retorna o maior de dois números
maior = lambda a, b: a if a > b else b

# 36. Aplicar função a cada elemento da lista
def aplicar_funcao(lista, func):
    return [func(x) for x in lista]