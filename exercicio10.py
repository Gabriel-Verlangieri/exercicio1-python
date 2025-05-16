#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
graus_fahrenheit = ((graus_celsius * 9) / 5) + 32

print(f"{graus_celsius} graus celsius correspondem a {graus_fahrenheit} graus fahrenheit")