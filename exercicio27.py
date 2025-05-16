#As Organizações Tabajara resolveram dar um aumento de salário aos seuscolaboradores e lhe contrataram para desenvolver o programa que calculará osreajustes.As Organizações Tabajara resolveram dar um aumento de salário aos seuscolaboradores e lhe contrataram para desenvolver o programa que calculará osreajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo oseguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%salários entre R$ 280,00 e R$ 700,00 : aumento de 15%salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%salários de R$ 1500,00 em diante :aumento de 5% Após o aumento ser realizado,
    

salario_anterior = float(input("Digite o salário atual: "))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280.0:
    percentual_de_aumento = 20

elif salario_anterior <= 700:
    percentual_de_aumento = 15

elif salario_anterior <= 1500:
    percentual_de_aumento = 10

else:
    percentual_de_aumento = 5

diferenca_entre_salarios = salario_anterior *(percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios

print(f"O salário antes do reajuste, era de R$ {salario_anterior:.2f}")
print(f"O seu salário foi aumentado para R$ {percentual_de_aumento:.2f}")
print(f" O valor do aumento foi de R$ {diferenca_entre_salarios:.2f}")
print(f" O novo salário será de R$ {salario_atual:.2f}")