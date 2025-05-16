# Faça um Programa que leia um número e exiba o dia correspondente da semana.(1-Domingo, 2- Segunda, etc.),se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite um número do dia da semana: "))
dia_str = ""

if dia == 1:
    dia_str = "Domingo"

elif dia == 2:
    dia_str = "Segunda"

elif dia == 3:
    dia_str = "Terça"

elif dia == 4:
    dia_str == "Quarta"

elif dia == 5:
    dia_str = "Quinta"

elif dia == 6:
    dia_str = "Sexta"

elif dia == 7:
    dia_str = "Sábado"

if dia_str == "":
    print("Valor Inválido")

else:
    print(f"O dia corresponde a: {dia_str}")