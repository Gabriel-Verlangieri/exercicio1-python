# Faça um Programa que peça os 3 lados de um triângulo.O programa deverá informar se os valores podem ser um triângulo.Indique, caso os lados formem um triângulo, se o mesmo é:equilátero, isósceles ou escaleno.
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (
    (lado1 + lado3 > lado2) 
    and (lado1 + lado2 > lado3)
    and (lado2 + lado3 > lado1)
    ):

 if (lado1 == lado2) and (lado2 == lado3):
    print("O triângulo é equilátero")

 elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("É um triângulo isósceles")

 else:
    print("É um triângulo escaleno")

else:
   print("Não é um triângulo")

