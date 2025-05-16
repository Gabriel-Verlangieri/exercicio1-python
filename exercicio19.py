# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite F para Feminino e M para Masculino: ")

if sexo == "F" or sexo == "Feminino":
    print("Feminino")

elif sexo == "M" or sexo == "Masculino":
    print("Masculino")

else:
    print("Sexo Inválido")