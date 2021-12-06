# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    #A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    #A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    #A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input("Digite nota parcial 1: "))
n2 = float(input("Digite nota parcial 2: "))
n3 = float(input("Digite nota parcial 3: "))

media = (n1+n2+n3)/3

if n1 >= 0 and n1 <=10 and n2 >= 0 and n2 <=10 and n3 >= 0 and n3 <=10:
    if media >= 7 and media < 10:
        print(f"Media do aluno: {media:.1f}")
        print("Aluno aprovado")
    
    elif media < 7:
        print(f"Media do aluno: {media:.1f}")
        print("Aluno Reprovado")

    else:
        print(f"Media do aluno: {media:.1f}")
        print("Aluno aprovado com distinção")

else:
    print("Nota invalida")