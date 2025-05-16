numero = int(input("Digite um número inteiro: "))

resultado = ""

if numero > 0:
    resultado = "Positivo"

elif numero == 0:
    resultado = "Nulo"

else:
    resultado = "Negativo"

print(resultado)