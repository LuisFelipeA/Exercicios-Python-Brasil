#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano para saber se ele é bissexto: "))

bi = ano%4

if bi == 0:
    print("O ano é bissexto")

else:
    print("O ano não é bissexto")
