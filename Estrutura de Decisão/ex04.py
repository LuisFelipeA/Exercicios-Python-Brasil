#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").upper()

contagem = len(letra)
n = letra.isnumeric()


if contagem == 1 and n == False:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("A letra Digitada é vogal")
    
    else:
        print("A letra digitada é Consoante")

elif n == True:
    print("Isso é um numero")

else:
    print("Digite novamente")