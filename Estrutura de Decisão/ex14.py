#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

p1 = float(input("Digite a nota parcial 1:"))
p2 = float(input("Digite a nota parcial 2:"))

media = (p1+p2)/2

if media >= 0 and media < 4:
    print("Nota 'E'")

elif media >= 4 and media < 6:
    print("Media'D'")
    
elif media >= 6 and media < 7.5:
    print("Media'C'")

elif media >= 7.5 and media < 9:
    print("Media'B'")
    
elif media >= 9 and media < 10:
    print("Media'A'")
    
elif media == 10:
    print("Media'A+'")

else:
    print("Nota invalida")