# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com menor preço é o 1, custando R$ {preco1:.2f}")

elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com menor preço foi o 2, custando R$ {preco2:.2f}")

else:
    print(f"O produto com menor preço foi o 3, custando R$ {preco3:.2f}")

