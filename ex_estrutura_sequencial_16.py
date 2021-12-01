#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
from math import ceil
area = float(input("Digite a area a ser pintada: m² "))
qtd_tinta = area/3
qtd_lata = qtd_tinta/18
qtd_lata_arredondado = math.ceil(qtd_lata)

valor = qtd_lata_arredondado*80

print(f"Quantidade de latas de 18 Litros: {qtd_lata_arredondado}")
print(f"Valor da compra: R${valor:.2f}")
