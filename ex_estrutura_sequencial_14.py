#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


peso_peixe = float(input("Digite o peso do peixe (Kg) "))

if peso_peixe > 50:
    peso_excesso = peso_peixe - 50

else:
    peso_excesso = 0      
    
multa = peso_excesso * 4    
print(f"Peso do peixe: {peso_peixe:.2f}Kg")
print(f"Excesso de peso: {peso_excesso:.2f}Kg")
print(f"Valor da multa: R${multa:.2f}")