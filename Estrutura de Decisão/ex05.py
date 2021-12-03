#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))

media = (nota1+nota2)/2

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
    print("Nota invalida. Digite novamente!")

else:
    if media >= 7 and media < 10:
        print(f"Media igual a {media:.1f}. Aluno aprovado!")

    elif media < 7:
        print(f"Media igual a {media:.1f}. Aluno Reprovado!")

    else:
        print(f"Media igual a {media:.1f}. Aluno Aprovado com Distinção!")
