# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: O produto do dobro do primeiro com a metade do segundo. A soma do triplo do primeiro com o terceiro. O terceiro elevado ao cubo

num1 = int(input("Digite um número inteiro: "))
num2 = int (input("Digite um número inteiro: "))
num3 = float(input("Digite um número real: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f"a: {a} b: {b} c: {c}")


