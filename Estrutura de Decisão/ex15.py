#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = float(input("Digite a primeiro lado: "))
b = float(input("Digite a segundo lado: "))
c = float(input("Digite a terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Triangulo Equilatero")

    elif a == b or b == c or a == c:
        print("Triangulo Isosceles")

    else:
        print("Triangulo Escaleno")

else:
    print("Nao é possivel formar um triangulo")