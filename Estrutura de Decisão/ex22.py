#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

n = int(input("Digite um numero para saber se é par ou impar: "))
par_impar = n%2

if par_impar == 1:
    print(f"O numero {n} é impar")

else:
    print(f"O numero {n} é par")