# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Digite um Dia: "))
mes = int(input("Digite um Mês: "))
ano = int(input("Digite um Ano: "))

if ano > 0 and ano < 9999:
    if mes >= 1 and mes <=12:
        if dia >= 1 and dia <=31:
            print("Data valida")
            print(f"A data digitada é {dia}/{mes}/{ano}")
        
        else:
            print("Data invalida")
    
    else:
        print("Data invalida")

else:
    print("Data invalida")