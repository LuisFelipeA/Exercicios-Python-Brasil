#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

pro1 = float(input("Digite o valor do produto 1: "))
pro2 = float(input("Digite o valor do produto 2: "))
pro3 = float(input("Digite o valor do produto 3: "))

if pro1 <= pro2 and pro1 <= pro3:
    print("Produto 1 é o mais barato")

elif pro2 <= pro1 and pro2 <= pro3:
    print("Produto 2 é o mais barato")

elif pro3 <= pro2 and pro3 <= pro1:
    print("Produto 3 é o mais barato")

else:
    print("Digite novamente")