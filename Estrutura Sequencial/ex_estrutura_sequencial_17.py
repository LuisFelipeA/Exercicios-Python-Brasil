# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
from math import ceil

area = float(input("Digite a area que vai ser pintada em m²: "))
qtd_tinta = area/6

qtd_lata = math.ceil(qtd_tinta/18)
qtd_galao = math.ceil(qtd_tinta/3.6)

qtd_lata_inteira = qtd_tinta // 18
qtd_lata_sobra = qtd_tinta % 18
qtd_galao_inteiro = math.ceil(qtd_lata_sobra/3.6)

valor_lata = 80
valor_galao = 25

valor_somente_latas = qtd_lata * valor_lata
valor_somente_galao = qtd_galao * valor_galao
valor_ambos = (qtd_lata_inteira * valor_lata) + (qtd_galao_inteiro * valor_galao)

print(f"Quantidade de latas:{qtd_lata} Valor: R${valor_somente_latas:.2f}")
print(f"Quantidade de galões:{qtd_galao} Valor: R${valor_somente_galao:.2f}")
print(f"Quantidade de latas e galões misturados: Latas{qtd_lata_inteira} e Galões:{qtd_galao_inteiro} Valor: R${valor_ambos:.2f}")