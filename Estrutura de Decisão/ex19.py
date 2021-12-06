# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero   = int(input("Digite um numero menor que 1000: "))

#converti para string para poder mostrar no print

if numero < 1000 and numero > 0:
    if numero < 100:
        if numero < 10:
            n = str(numero)
            print(f"{n[0]} unidade(s)")
        
        else:
            n = str(numero)
            print(f"{n[0]} dezena(s) e {n[1]} unidade(s)")
    
    else:
        n = str(numero)
        print(f"{n[0]} centena(s), {n[1]} dezena(s) e {n[2]} unidade(s)")

else:
    print("Valor invalido")