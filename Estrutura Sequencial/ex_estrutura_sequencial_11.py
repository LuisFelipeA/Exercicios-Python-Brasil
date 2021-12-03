#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#.o produto do dobro do primeiro com metade do segundo .
#.a soma do triplo do primeiro com o terceiro.
#.o terceiro elevado ao cubo.

n1 = int(input("Digite um numero 1 (inteiro):"))
n2 = int(input("Digite um numero 2 (inteiro):"))
n3 =n1 = float(input("Digite um numero 3 (real):"))

produto = (n1*2)*(n2/2)
soma = (n1*3)+n3
cubo = n3**3

print(f"O produto do dobro do primeiro com metade do segundo é {produto:.2f}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma:.2f}")
print(f"O terceiro elevado ao cubo é: {cubo:.2f}")