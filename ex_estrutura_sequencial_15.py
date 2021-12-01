# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a)salário bruto.
# b)quanto pagou ao INSS.
# c)quanto pagou ao sindicato.
# d)o salário líquido.
# e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
#    Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas trabalhou? "))

salario_bruto = ganho_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_desconto = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - total_desconto

print("-"*20)
print(f"Salario Bruto: R${salario_bruto:.2f}")
print(f"Pagou de imposto de renda: R${imposto_renda:.2f}")
print(f"Pagou ao INSS: R${inss:.2f}")
print(f"Pagou ao Sindicato: R${sindicato:.2f}")
print("-"*20)
print(f"Salario Liquido: R${salario_liquido:.2f}")
print("-"*20)