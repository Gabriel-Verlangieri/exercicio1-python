#  Faça um programa que calcule a área de um quadrado e em seguida mostre o dobro desta área para o usuário

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro = area * 2

print(f"O dobro da área de um quadrado de lado {lado} é {dobro}")