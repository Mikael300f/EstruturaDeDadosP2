# 22. Contar quantas vezes uma letra aparece em uma string
def contar_letra(texto, letra):
    return texto.count(letra)

# 23. Verificar se uma palavra é um palíndromo
def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

# 24. Substituir todas as ocorrências de uma letra por outra
def substituir_letra(texto, original, nova):
    return texto.replace(original, nova)