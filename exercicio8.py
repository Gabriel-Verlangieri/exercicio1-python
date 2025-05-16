#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhados no mês. Calcule e mostre o total do seu salário no referido mês

salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_total = salario_hora * horas_trabalhadas_mes

print(f"O total do salário no mês foi de {salario_hora} + {horas_trabalhadas_mes} = {salario_total} reais")