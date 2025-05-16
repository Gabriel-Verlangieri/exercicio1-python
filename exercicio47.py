# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando apedir as informações.

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha do usuário: ")

while usuario == senha:
    print("Nome de usuário não pode ser igual a senha")

    usuario = input("Digite novamente o nome do usuário: ")
    senha = input("Digite novamente a senha do usuário: ")