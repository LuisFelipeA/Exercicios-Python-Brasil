# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite outro numero: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"Ordem decrescente: {n1}, {n2} e {n3}")
    else:
        print(f"Ordem decrescente: {n1}, {n3} e {n2}")

elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"Ordem decrescente: {n2}, {n1} e {n3}")
    else:
        print(f"Ordem decrescente: {n2}, {n3} e {n1}")

elif n3 > n2 and n3 > n1:
    if n2 > n1:
        print(f"Ordem decrescente: {n3}, {n2} e {n1}")
    else:
        print(f"Ordem decrescente: {n3}, {n1} e {n2}")

else:
    print("Digite novamente")
