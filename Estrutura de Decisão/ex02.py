#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input("Digite um numero: "))

if n1 > 0 :
    print(f"O numero {n1} é positivo")

elif n1 < 0 :
    print(f"O numero {n1} é negativo")

else:
    print(f"O numero {n1} não é positivo nem negativo")
