# 19. Divisão com tratamento de divisão por zero
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

# 20. Conversão de string para inteiro com tratamento de erro
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return "Erro: entrada não é um número inteiro"

# 21. Abrir arquivo para leitura com tratamento de erro
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Erro: arquivo não encontrado"