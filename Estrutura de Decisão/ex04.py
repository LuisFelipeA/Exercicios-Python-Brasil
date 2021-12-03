#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").upper()

contagem = len(letra)
n = letra.isalpha()

if contagem == 1 and n == True:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("A letra Digitada é vogal")
    
    else:
        print("A letra digitada é Consoante")

else:
    print("Digite somente letras")