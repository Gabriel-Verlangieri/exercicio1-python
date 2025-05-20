# Faça um contador de 1 a 100
for i in range(1,101):
    print(i)

# Faça um contador progressivo de 1 a 20 de 2 em 2

for i in range(1,21,2):
    print(i)

# Faça um contador regressivo de 100 a 1

for i in range(100,0,-1):
    print(i)

# Faça um contador regressivo de 200 a 100 de 2 em 2

for i in range(200,98,-2):
    print(i)

# Faça um algoritmo que conte de 1 a 10, verifique se é par e faça a soma dos pares
soma_pares = 0
for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")
        soma_pares += i
        print(soma_pares)

