# Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue pedindo até que ousuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota > 10 or nota < 0:

    nota = float(input("Valor inválido. Favor, digite uma nota válida entre 0 e 10: "))
