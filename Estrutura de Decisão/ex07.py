#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite mais um numero: "))
n3 = float(input("Digite mais um numero: "))

if n1 >= n2 and n1 >= n3:
    if n2 > n3:
        print(f"O numero {n1} é o maior e {n3} é o menor")
    else:
        print(f"O numero {n1} é o maior e {n2} é o menor")

elif n2 >= n1 and n2 >= n3:
    if n1 > n3:
        print(f"O numero {n2} é o maior e {n3} é o menor")
    else:
        print(f"O numero {n2} é o maior e {n1} é o menor")

elif n3 >= n1 and n3 >= n2:
    if n1 > n2:
        print(f"O numero {n3} é o maior e {n2} é o menor")
    else:
        print(f"O numero {n3} é o maior e {n1} é o menor")