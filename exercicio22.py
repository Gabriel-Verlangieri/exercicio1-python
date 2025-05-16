# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite o último número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} foi o maior número digitado")

elif num2 > num1 and num2 > num3:
    print(f"{num2} foi o maior número digitado")

else:
    print(f"{num3} foi o maior número digitado")