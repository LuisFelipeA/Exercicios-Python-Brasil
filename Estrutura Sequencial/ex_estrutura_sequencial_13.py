#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#.Para homens: (72.7*h) - 58
#.Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura (em Metros): "))

repete = True

while repete == True:


    sexo = input("Digite seu sexo: (F = Feminino e M = Masculino) ")

    if sexo == "M" or sexo == "m":
        peso_ideal = (72.7*altura) - 58
        print(f"Seu peso ideal é {peso_ideal:.2f}Kg")
        repete = False

    elif sexo == "F" or sexo == "f":
        peso_ideal =  (62.1*altura) - 44.7
        print(f"Seu peso ideal é {peso_ideal:.2f}Kg")
        repete = False
    else:
        print("Sexo invalido! Digite novamente:")
