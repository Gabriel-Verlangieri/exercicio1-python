# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} foi o maior número digitado")

elif num2 > num1 and num2 > num3:
    print(f"{num2} foi o maior número digitado")

else:
    print(f"{num3} foi o maior número digitado")


if num1 < num2 and num1 < num3:
    print(f"{num1} foi o menor número digitado")

elif num2 < num1 and num2 < num3:
    print(f"{num2} foi o menor número digitado")

else:
    print(f"{num3} foi o menor número digitado")