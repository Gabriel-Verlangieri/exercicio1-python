# For Loop - Contagem Progressiva: Crie um programa que utiliza o loop for para imprimir uma contagem de 10 a 30.

for i in range(10,31):
    print(i)

# While Loop - Contagem Regressiva: Faça um programa que utiliza o loop while para imprimir uma contagem regressiva de 10 a 1.

for i in range(10,1,-1):
    print(i)

# For Loop - Soma Pares: Crie um programa que utiliza o loop for para calcular a soma dos números pares de 1 a 50.

soma_pares = 0
for i in range(1,51,2):
    print(i)
    
# While Loop - Fatorial: Implemente um programa que calcula o fatorial de um número usando o loop while.

soma = 0

for numero in range(1,51):
    if numero % 2 == 0:
        soma  += numero

        print(f"A soma dos números pares de 1 a 50 é: {soma}")


# Implemente um programa que calcula o fatorial de um número usando o loop while.

num1 = int(input("Digite um número inteiro não negativo: "))

if num1 < 0:
    print("Fatorial não definido")
else:
    fatorial = 1
    contador = num1
    while contador > 1:
        fatorial *= contador - 1

print(f"O fatorial de um número é: {fatorial}")

# Quadrados: Utilize o loop for para imprimir os quadrados dos números de 1 a 20.

for i in range(1,21):
    print(f"O quadrado de {i} é {i**2}")

#  Soma Ímpares: Implemente um programa que utiliza o loop while para calcular a soma dos números ímpares de 1 a 50.
soma_impar = 1
for i in range(1,51):
    if i %  3 == 1:
        print(f"{i} é ímpar")
        soma_impar +=1
        print(soma_impar)
