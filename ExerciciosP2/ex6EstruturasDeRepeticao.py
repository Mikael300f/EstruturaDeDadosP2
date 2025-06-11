# 16
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# 17
n = int(input("Digite um número: "))
soma = 0
for i in range(1, n+1):
    soma += i
print("Soma:", soma)

# 18
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")