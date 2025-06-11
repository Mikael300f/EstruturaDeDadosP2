# 13
numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")

# 14
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))
if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
else:
    print("Escaleno")

# 15
saldo = 1000
saque = float(input("Valor do saque: "))
if saque <= saldo:
    saldo -= saque
    print("Saque realizado. Novo saldo:", saldo)
else:
    print("Saldo insuficiente")