#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
#Utilize as fórmulas para homem: (72.7*h) - 58
#mulher: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(f"O peso ideal para homens é de: {peso_ideal_homem} kg")
print(f"O peso ideal para mulher é de: {peso_ideal_mulher} kg")
