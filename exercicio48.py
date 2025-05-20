# Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 caracteres;   Idade: entre 0 e 150; Salário: maior que zero;Sexo: 'f' ou 'm';Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o nome: ")
while len (nome) < 4:
    print("Nome inválido")
    nome = (input("Digite seu nome novamente: "))

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida")
    idade = input("Digite novamente a idade: ")

salario = int(input("Digite o salário: "))
while salario <= 0:
    print("Salário inválido")
    salario = input("Digite novamente o salário: ")

sexo = input("Digite o sexo (f ou m): ")
while sexo  != "f" and sexo !="m":
    print("Sexo inválido")
    sexo = ("Digite novamente o sexo (f ou m)")

estado_civil = input("Digite o estado civil (s,c,v,d)")
while estado_civil !="s" and estado_civil !="c" and estado_civil !="v" and estado_civil !="d":
    print("Estado civil inválido")
    estado_civil = ("Digite o estado civil novamente (s,c,v,d): ")


