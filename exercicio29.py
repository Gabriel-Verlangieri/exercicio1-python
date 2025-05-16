# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
aproveitamento = ""

if media >=9:
    aproveitamento ="A"

elif media >=7.5:
    aproveitamento = "B"

elif media >=6:
    aproveitamento = "C"

elif media >=4:
    aproveitamento = "D"

else:
    aproveitamento = "E"

if aproveitamento == "D" or aproveitamento == "E":
    print(f"Reprovado" {aproveitamento})

else:
    print(f"Aprovado" {aproveitamento})